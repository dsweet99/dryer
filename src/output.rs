use crate::edit_distance::Duplicate;
use crate::scoring::{FeatureVector, ScoringConfig};
use std::collections::HashMap;
use std::io::{self, Write};
use std::path::Path;

/// Union-Find data structure for clustering
struct UnionFind {
    parent: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self { parent: (0..n).collect() }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]); // path compression
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let px = self.find(x);
        let py = self.find(y);
        if px != py {
            self.parent[px] = py;
        }
    }
}

/// A location in the codebase (file + line range)
#[derive(Clone, Hash, Eq, PartialEq)]
struct Location {
    file: String,
    start: usize,
    end: usize,
}

/// Extended location data including metrics for scoring
struct LocationData {
    loc: Location,
    text: String,
    char_count: usize,
    file_offset: usize,
    line_count: usize,
}

impl Location {
    fn display(&self) -> String {
        format!("{}:{}-{}", self.file, self.start, self.end)
    }
}

/// Check if a chunk's file path matches any of the filter files
fn matches_filter(chunk_file: &Path, scan_root: &Path, filter_files: &[impl AsRef<Path>]) -> bool {
    if filter_files.is_empty() {
        return true;
    }
    
    for filter in filter_files {
        let filter_path = filter.as_ref();
        
        // Try matching as-is
        if chunk_file == filter_path {
            return true;
        }
        
        // Try matching filter relative to scan root
        let full_filter = scan_root.join(filter_path);
        if chunk_file == full_filter {
            return true;
        }
        
        // Try suffix matching (chunk path ends with filter path)
        if chunk_file.ends_with(filter_path) {
            return true;
        }
    }
    
    false
}

/// Filter duplicates to only include those involving at least one filter file
fn filter_duplicates<'a>(
    duplicates: &'a [Duplicate],
    scan_root: &Path,
    filter_files: &[impl AsRef<Path>],
) -> Vec<&'a Duplicate> {
    if filter_files.is_empty() {
        return duplicates.iter().collect();
    }
    
    duplicates
        .iter()
        .filter(|dup| {
            matches_filter(&dup.chunk1.file, scan_root, filter_files)
                || matches_filter(&dup.chunk2.file, scan_root, filter_files)
        })
        .collect()
}

/// Cluster duplicates and print grouped output
#[allow(clippy::too_many_lines)] // Logic is cohesive; splitting would harm readability
pub fn print_duplicates(duplicates: &[Duplicate], verbose: bool, scan_root: &Path, filter_files: &[impl AsRef<Path>]) {
    let stdout = io::stdout();
    let mut out = stdout.lock();

    let filtered = filter_duplicates(duplicates, scan_root, filter_files);
    
    if filtered.is_empty() {
        return;
    }

    // Load scoring configuration
    let scoring_config = ScoringConfig::load();

    // Build location index with extended data
    let mut loc_to_idx: HashMap<Location, usize> = HashMap::new();
    let mut idx_to_data: Vec<LocationData> = Vec::new();

    for dup in &filtered {
        for chunk in [&dup.chunk1, &dup.chunk2] {
            let loc = Location {
                file: chunk.file.display().to_string(),
                start: chunk.start_line,
                end: chunk.end_line,
            };
            if !loc_to_idx.contains_key(&loc) {
                let idx = idx_to_data.len();
                loc_to_idx.insert(loc.clone(), idx);
                idx_to_data.push(LocationData {
                    loc,
                    text: chunk.original.clone(),
                    char_count: chunk.original.len(),
                    file_offset: chunk.file_offset,
                    line_count: chunk.end_line - chunk.start_line + 1,
                });
            }
        }
    }

    // Union-find clustering and track edit distances per pair
    let mut uf = UnionFind::new(idx_to_data.len());
    let mut pair_distances: HashMap<(usize, usize), f64> = HashMap::new();
    
    for dup in &filtered {
        let loc1 = Location {
            file: dup.chunk1.file.display().to_string(),
            start: dup.chunk1.start_line,
            end: dup.chunk1.end_line,
        };
        let loc2 = Location {
            file: dup.chunk2.file.display().to_string(),
            start: dup.chunk2.start_line,
            end: dup.chunk2.end_line,
        };
        let idx1 = loc_to_idx[&loc1];
        let idx2 = loc_to_idx[&loc2];
        uf.union(idx1, idx2);
        let key = (idx1.min(idx2), idx1.max(idx2));
        pair_distances.insert(key, dup.normalized_distance);
    }

    // Group by cluster root
    let mut clusters: HashMap<usize, Vec<usize>> = HashMap::new();
    for idx in 0..idx_to_data.len() {
        let root = uf.find(idx);
        clusters.entry(root).or_default().push(idx);
    }

    // Calculate mean distance for a location within its cluster
    let mean_distance_for_idx = |idx: usize, cluster: &[usize]| -> f64 {
        let mut total = 0.0;
        let mut count: i32 = 0;
        for &other_idx in cluster {
            if other_idx != idx {
                let key = (idx.min(other_idx), idx.max(other_idx));
                if let Some(&dist) = pair_distances.get(&key) {
                    total += dist;
                    count += 1;
                }
            }
        }
        if count > 0 { total / f64::from(count) } else { 0.0 }
    };

    // Compute feature vector and score for a location
    let compute_score = |idx: usize, cluster: &[usize]| -> f64 {
        let data = &idx_to_data[idx];
        let features = FeatureVector {
            cluster_size: cluster.len(),
            mean_distance: mean_distance_for_idx(idx, cluster),
            char_count: data.char_count,
            file_offset: data.file_offset,
            line_count: data.line_count,
        };
        scoring_config.score(&features)
    };

    // Compute cluster score as average of member scores
    #[allow(clippy::cast_precision_loss)] // Cluster sizes are small enough
    let cluster_score = |cluster: &[usize]| -> f64 {
        let total: f64 = cluster.iter().map(|&idx| compute_score(idx, cluster)).sum();
        total / cluster.len() as f64
    };

    // Sort clusters by score (highest first, since higher score = more important)
    let mut cluster_list: Vec<_> = clusters.into_values().filter(|c| c.len() > 1).collect();
    cluster_list.sort_by(|a, b| {
        cluster_score(b)
            .partial_cmp(&cluster_score(a))
            .unwrap_or(std::cmp::Ordering::Equal)
    });

    // Print clusters
    for cluster in &cluster_list {
        let score = cluster_score(cluster);
        if verbose {
            writeln!(out, "=== {} locations (score {:.3}) ===", cluster.len(), score).unwrap();
            for &idx in cluster {
                let data = &idx_to_data[idx];
                let loc_score = compute_score(idx, cluster);
                writeln!(out, "--- {} (score {:.3}):", data.loc.display(), loc_score).unwrap();
                for line in data.text.lines() {
                    writeln!(out, "  {line}").unwrap();
                }
                writeln!(out).unwrap();
            }
        } else {
            let locations: Vec<_> = cluster.iter().map(|&idx| idx_to_data[idx].loc.display()).collect();
            writeln!(out, "{:.3}  {}", score, locations.join("  ")).unwrap();
        }
    }
}
