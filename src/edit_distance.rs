#![allow(clippy::cast_precision_loss)] // Intentional: normalized distances use f64

use crate::chunker::Chunk;
use crate::config::Config;
use crate::lsh::CandidatePair;
use crate::minhash::Signature;
use rayon::prelude::*;
use triple_accel::levenshtein::levenshtein_simd_k;

#[derive(Debug, Clone)]
pub struct Duplicate {
    pub chunk1: Chunk,
    pub chunk2: Chunk,
    pub edit_distance: usize,
    pub normalized_distance: f64,
}

const MIN_JACCARD_SIMILARITY: f64 = 0.4;

pub fn verify_candidates(
    chunks: &[Chunk],
    signatures: &[Signature],
    candidates: &[CandidatePair],
    config: &Config,
) -> Vec<Duplicate> {
    candidates
        .par_iter()
        .filter_map(|pair| {
            let first_chunk = &chunks[pair.idx1];
            let second_chunk = &chunks[pair.idx2];

            let is_same_file = first_chunk.file == second_chunk.file;
            if is_same_file && ranges_overlap(first_chunk, second_chunk) {
                return None;
            }

            let sig1 = &signatures[pair.idx1];
            let sig2 = &signatures[pair.idx2];
            let matching = sig1.hashes.iter().zip(&sig2.hashes).filter(|(a, b)| a == b).count();
            let estimated_jaccard = matching as f64 / sig1.hashes.len() as f64;
            if estimated_jaccard < MIN_JACCARD_SIMILARITY {
                return None;
            }

            let a = first_chunk.normalized.as_bytes();
            let b = second_chunk.normalized.as_bytes();
            let max_len = a.len().max(b.len());

            if max_len == 0 {
                return Some(Duplicate {
                    chunk1: first_chunk.clone(),
                    chunk2: second_chunk.clone(),
                    edit_distance: 0,
                    normalized_distance: 0.0,
                });
            }

            let len_diff = a.len().abs_diff(b.len());
            if len_diff as f64 / max_len as f64 > config.edit_threshold {
                return None;
            }

            #[allow(clippy::cast_possible_truncation, clippy::cast_sign_loss)]
            let max_allowed = (config.edit_threshold * max_len as f64).ceil() as u32;
            let byte_edit_distance = match levenshtein_simd_k(a, b, max_allowed) {
                Some(dist) => dist as usize,
                None => return None,
            };

            let normalized_by_bytes = byte_edit_distance as f64 / max_len as f64;

            if normalized_by_bytes > config.edit_threshold {
                return None;
            }

            Some(Duplicate {
                chunk1: first_chunk.clone(),
                chunk2: second_chunk.clone(),
                edit_distance: byte_edit_distance,
                normalized_distance: normalized_by_bytes,
            })
        })
        .collect()
}

const fn ranges_overlap(c1: &Chunk, c2: &Chunk) -> bool {
    !(c1.end_line < c2.start_line || c2.end_line < c1.start_line)
}

pub fn levenshtein_bytes(a: &str, b: &str) -> usize {
    triple_accel::levenshtein(a.as_bytes(), b.as_bytes()) as usize
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::path::PathBuf;
    use std::sync::Arc;

    #[test]
    fn test_levenshtein_distances() {
        // (input_a, input_b, expected_distance)
        let cases = [
            ("hello", "hello", 0),  // identical
            ("hello", "hallo", 1),  // one substitution
            ("hello", "helllo", 1), // one insertion
            ("hello", "helo", 1),   // one deletion
        ];
        for (a, b, expected) in cases {
            assert_eq!(levenshtein_bytes(a, b), expected, "{a} vs {b}");
        }
    }

    #[test]
    fn test_normalized_distance() {
        let dist = levenshtein_bytes("hello", "hallo");
        let max_len = 5;
        let normalized = dist as f64 / f64::from(max_len);
        assert!((normalized - 0.2).abs() < 0.001);
    }

    use crate::test_utils::{config_with_threshold, make_chunk};

    /// Helper to create a Chunk with just line range (for `ranges_overlap` tests)
    fn chunk_range(start: usize, end: usize) -> Chunk {
        Chunk {
            file: Arc::new(PathBuf::from("test.py")),
            start_line: start,
            end_line: end,
            file_offset: 0,
            original: String::new(),
            normalized: String::new(),
        }
    }

    #[test]
    fn test_ranges_overlap_disjoint() {
        let (c1, c2) = (chunk_range(1, 5), chunk_range(10, 15));
        assert!(!ranges_overlap(&c1, &c2));
        assert!(!ranges_overlap(&c2, &c1));
    }

    #[test]
    fn test_ranges_overlap_touching() {
        let (c1, c2) = (chunk_range(1, 5), chunk_range(5, 10));
        assert!(ranges_overlap(&c1, &c2));
    }

    #[test]
    fn test_ranges_overlap_fully_contained() {
        let (c1, c2) = (chunk_range(1, 20), chunk_range(5, 10));
        assert!(ranges_overlap(&c1, &c2));
        assert!(ranges_overlap(&c2, &c1));
    }

    #[test]
    fn test_ranges_overlap_partial() {
        let (c1, c2) = (chunk_range(1, 10), chunk_range(8, 15));
        assert!(ranges_overlap(&c1, &c2));
    }

    fn mock_signatures(count: usize) -> Vec<Signature> {
        (0..count).map(|_| Signature { hashes: vec![1, 2, 3, 4].into_boxed_slice() }).collect()
    }

    /// Helper to run verification on a pair of chunks with default test setup
    fn verify_pair(chunks: &[Chunk]) -> Vec<Duplicate> {
        let signatures = mock_signatures(chunks.len());
        let candidates = vec![CandidatePair { idx1: 0, idx2: 1 }];
        let config = config_with_threshold(0.15);
        verify_candidates(chunks, &signatures, &candidates, &config)
    }

    #[test]
    fn test_verify_candidates_finds_identical() {
        let dups = verify_pair(&[
            make_chunk("a.py", 1, 5, "hello world"),
            make_chunk("b.py", 1, 5, "hello world"),
        ]);
        assert_eq!(dups.len(), 1);
        assert_eq!(dups[0].edit_distance, 0);
        assert!(dups[0].normalized_distance.abs() < f64::EPSILON);
    }

    #[test]
    fn test_verify_candidates_finds_similar() {
        let dups = verify_pair(&[
            make_chunk("a.py", 1, 5, "hello world"),
            make_chunk("b.py", 1, 5, "hallo world"),
        ]);
        assert_eq!(dups.len(), 1);
        assert_eq!(dups[0].edit_distance, 1);
        assert!((dups[0].normalized_distance - 1.0 / 11.0).abs() < 0.01);
    }

    #[test]
    fn test_verify_candidates_filters_by_threshold() {
        let dups = verify_pair(&[
            make_chunk("a.py", 1, 5, "hello"),
            make_chunk("b.py", 1, 5, "world"),
        ]);
        assert!(dups.is_empty());
    }

    #[test]
    fn test_verify_candidates_skips_overlapping_same_file() {
        let dups = verify_pair(&[
            make_chunk("same.py", 1, 10, "hello world"),
            make_chunk("same.py", 5, 15, "hello world"),
        ]);
        assert!(dups.is_empty());
    }

    #[test]
    fn test_verify_candidates_allows_nonoverlapping_same_file() {
        let dups = verify_pair(&[
            make_chunk("same.py", 1, 5, "hello world"),
            make_chunk("same.py", 10, 15, "hello world"),
        ]);
        assert_eq!(dups.len(), 1);
    }

    #[test]
    fn test_verify_candidates_empty_input() {
        let chunks: Vec<Chunk> = vec![];
        let signatures: Vec<Signature> = vec![];
        let candidates: Vec<CandidatePair> = vec![];
        let config = config_with_threshold(0.15);
        let dups = verify_candidates(&chunks, &signatures, &candidates, &config);
        assert!(dups.is_empty());
    }

    #[test]
    fn test_verify_candidates_handles_empty_strings() {
        let dups = verify_pair(&[
            make_chunk("a.py", 1, 1, ""),
            make_chunk("b.py", 1, 1, ""),
        ]);
        assert_eq!(dups.len(), 1);
        assert!(dups[0].normalized_distance.abs() < f64::EPSILON);
    }

    #[test]
    fn test_regression_levenshtein_operates_on_bytes() {
        assert_eq!(levenshtein_bytes("hello", "hallo"), 1);
        assert_eq!("hello".len(), 5);
        assert_eq!("hello".chars().count(), 5);

        let hello_ascii = "hello";
        let hello_accented = "héllo";
        assert_eq!(hello_ascii.len(), 5);
        assert_eq!(hello_accented.len(), 6);
        assert_eq!(hello_accented.chars().count(), 5);

        let dist = levenshtein_bytes(hello_ascii, hello_accented);
        assert_eq!(dist, 2, "Byte-based edit distance: 'e'->'\u{00e9}' = 2 edits");
    }

    #[test]
    fn test_regression_normalized_distance_uses_byte_length() {
        let ascii = "test";
        let emoji = "test🎉";

        let dist = levenshtein_bytes(ascii, emoji);
        let normalized_by_bytes = dist as f64 / ascii.len().max(emoji.len()) as f64;
        let normalized_by_chars = dist as f64 / ascii.chars().count().max(emoji.chars().count()) as f64;

        assert_eq!(ascii.len().max(emoji.len()), 8);
        assert_eq!(ascii.chars().count().max(emoji.chars().count()), 5);

        assert!(
            (normalized_by_bytes - normalized_by_chars).abs() > 0.01,
            "Byte vs char normalization should differ for emoji"
        );
    }
}
