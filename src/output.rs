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

    // Union-find clustering
    let mut uf = UnionFind::new(idx_to_loc.len());
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
    }

    // Group by cluster root
    let mut clusters: HashMap<usize, Vec<usize>> = HashMap::new();
    for idx in 0..idx_to_loc.len() {
        let root = uf.find(idx);
        clusters.entry(root).or_default().push(idx);
    }

    // Sort clusters by size (largest first)
    let mut cluster_list: Vec<_> = clusters.into_values().filter(|c| c.len() > 1).collect();
    cluster_list.sort_by_key(|c| std::cmp::Reverse(c.len()));

    // Print clusters
    for (i, cluster) in cluster_list.iter().enumerate() {
        writeln!(out, "=== Cluster {} ({} locations) ===", i + 1, cluster.len()).unwrap();
        for &idx in cluster {
            writeln!(out, "  {}", idx_to_loc[idx].display()).unwrap();
        }
        
        if verbose {
            writeln!(out, "--- sample:").unwrap();
            let sample_idx = cluster[0];
            for line in idx_to_text[sample_idx].lines() {
                writeln!(out, "  {line}").unwrap();
            }
        }
        writeln!(out).unwrap();
    }

    writeln!(out, "Total: {} clusters from {} locations", cluster_list.len(), idx_to_loc.len()).unwrap();
}
