use crate::edit_distance::Duplicate;
use std::collections::HashMap;
use std::io::{self, Write};

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

impl Location {
    fn display(&self) -> String {
        format!("{}:{}-{}", self.file, self.start, self.end)
    }
}

/// Cluster duplicates and print grouped output
pub fn print_duplicates(duplicates: &[Duplicate], verbose: bool) {
    let stdout = io::stdout();
    let mut out = stdout.lock();

    if duplicates.is_empty() {
        return;
    }

    // Build location index
    let mut loc_to_idx: HashMap<Location, usize> = HashMap::new();
    let mut idx_to_loc: Vec<Location> = Vec::new();
    let mut idx_to_text: Vec<String> = Vec::new();

    for dup in duplicates {
        for (file, start, end, text) in [
            (&dup.chunk1.file, dup.chunk1.start_line, dup.chunk1.end_line, &dup.chunk1.original),
            (&dup.chunk2.file, dup.chunk2.start_line, dup.chunk2.end_line, &dup.chunk2.original),
        ] {
            let loc = Location {
                file: file.display().to_string(),
                start,
                end,
            };
            if !loc_to_idx.contains_key(&loc) {
                let idx = idx_to_loc.len();
                loc_to_idx.insert(loc.clone(), idx);
                idx_to_loc.push(loc);
                idx_to_text.push(text.clone());
            }
        }
    }

    // Union-find clustering and track scores per pair
    let mut uf = UnionFind::new(idx_to_loc.len());
    let mut pair_scores: HashMap<(usize, usize), f64> = HashMap::new();
    
    for dup in duplicates {
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
        pair_scores.insert(key, dup.normalized_distance);
    }

    // Group by cluster root
    let mut clusters: HashMap<usize, Vec<usize>> = HashMap::new();
    for idx in 0..idx_to_loc.len() {
        let root = uf.find(idx);
        clusters.entry(root).or_default().push(idx);
    }

    // Calculate average score per cluster
    let cluster_avg_score = |cluster: &[usize]| -> f64 {
        let mut total = 0.0;
        let mut count = 0;
        for i in 0..cluster.len() {
            for j in (i + 1)..cluster.len() {
                let key = (cluster[i].min(cluster[j]), cluster[i].max(cluster[j]));
                if let Some(&score) = pair_scores.get(&key) {
                    total += score;
                    count += 1;
                }
            }
        }
        if count > 0 { total / f64::from(count) } else { 0.0 }
    };

    // Sort clusters by average score (lowest/best first)
    let mut cluster_list: Vec<_> = clusters.into_values().filter(|c| c.len() > 1).collect();
    cluster_list.sort_by(|a, b| {
        cluster_avg_score(a)
            .partial_cmp(&cluster_avg_score(b))
            .unwrap_or(std::cmp::Ordering::Equal)
    });

    // Print clusters
    for cluster in &cluster_list {
        let avg_score = cluster_avg_score(cluster);
        if verbose {
            writeln!(out, "=== {} locations (avg {:.3}) ===", cluster.len(), avg_score).unwrap();
            for &idx in cluster {
                writeln!(out, "--- {}:", idx_to_loc[idx].display()).unwrap();
                for line in idx_to_text[idx].lines() {
                    writeln!(out, "  {line}").unwrap();
                }
                writeln!(out).unwrap();
            }
        } else {
            let locations: Vec<_> = cluster.iter().map(|&idx| idx_to_loc[idx].display()).collect();
            writeln!(out, "{:.3}  {}", avg_score, locations.join("  ")).unwrap();
        }
    }
}
