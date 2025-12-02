use crate::config::Config;
use crate::minhash::Signature;
use rustc_hash::{FxBuildHasher, FxHashMap};

#[derive(Debug, Clone, Copy, Hash, Eq, PartialEq)]
pub struct CandidatePair {
    pub idx1: usize,
    pub idx2: usize,
}

pub fn find_candidates(signatures: &[Signature], config: &Config) -> Vec<CandidatePair> {
    let num_bands = config.lsh_bands;
    let rows_per_band = (config.minhash_size / num_bands).max(1);

    if config.minhash_size < num_bands {
        eprintln!(
            "Warning: minhash_size ({}) < lsh_bands ({}), using 1 row per band",
            config.minhash_size, num_bands
        );
    }

    let estimated_candidates = (signatures.len() / 10).max(1000);
    let mut candidates = rustc_hash::FxHashSet::with_capacity_and_hasher(
        estimated_candidates,
        FxBuildHasher,
    );

    for band_idx in 0..num_bands {
        let band_start = band_idx * rows_per_band;
        let band_end = (band_start + rows_per_band).min(config.minhash_size);

        if band_start >= config.minhash_size {
            break;
        }

        let mut band_buckets: FxHashMap<u64, Vec<usize>> = FxHashMap::default();

        for (idx, sig) in signatures.iter().enumerate() {
            let band_hash = hash_band(&sig.hashes[band_start..band_end]);
            band_buckets.entry(band_hash).or_default().push(idx);
        }

        for indices_in_bucket in band_buckets.values() {
            add_pairs_from_bucket(indices_in_bucket, &mut candidates);
        }
    }

    candidates.into_iter().collect()
}

const MAX_BUCKET_SIZE: usize = 200;

fn add_pairs_from_bucket(indices: &[usize], candidates: &mut rustc_hash::FxHashSet<CandidatePair>) {
    if indices.len() < 2 {
        return;
    }
    if indices.len() > MAX_BUCKET_SIZE {
        return;
    }
    for i in 0..indices.len() {
        for j in (i + 1)..indices.len() {
            let (smaller, larger) = (indices[i].min(indices[j]), indices[i].max(indices[j]));
            candidates.insert(CandidatePair { idx1: smaller, idx2: larger });
        }
    }
}

fn hash_band(band: &[u64]) -> u64 {
    use std::hash::{Hash, Hasher};
    let mut hasher = rustc_hash::FxHasher::default();
    band.hash(&mut hasher);
    hasher.finish()
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::test_utils::config_with_lsh;

    fn make_sig(hashes: Vec<u64>) -> Signature {
        Signature { hashes: hashes.into_boxed_slice() }
    }

    #[test]
    fn test_identical_sigs_are_candidates() {
        let config = config_with_lsh(8, 4);

        let sigs = vec![
            make_sig(vec![1, 2, 3, 4, 5, 6, 7, 8]),
            make_sig(vec![1, 2, 3, 4, 5, 6, 7, 8]),
            make_sig(vec![100, 200, 300, 400, 500, 600, 700, 800]),
        ];

        let candidates = find_candidates(&sigs, &config);

        assert!(candidates.contains(&CandidatePair { idx1: 0, idx2: 1 }));
        assert!(!candidates.contains(&CandidatePair { idx1: 0, idx2: 2 }));
    }

    #[test]
    fn test_empty_signatures_returns_empty() {
        let config = config_with_lsh(8, 4);
        let sigs: Vec<Signature> = vec![];
        let candidates = find_candidates(&sigs, &config);
        assert!(candidates.is_empty());
    }

    #[test]
    fn test_single_signature_returns_empty() {
        let config = config_with_lsh(8, 4);
        let sigs = vec![make_sig(vec![1, 2, 3, 4, 5, 6, 7, 8])];
        let candidates = find_candidates(&sigs, &config);
        assert!(candidates.is_empty());
    }

    /// Helper: find candidates using standard (8, 4) config
    fn candidates_8_4(sig_data: &[Vec<u64>]) -> Vec<CandidatePair> {
        let sigs: Vec<_> = sig_data.iter().map(|v| make_sig(v.clone())).collect();
        find_candidates(&sigs, &config_with_lsh(8, 4))
    }

    #[test]
    fn test_partial_band_match_creates_candidate() {
        // First two hash values match (one band) → should be candidates
        let candidates = candidates_8_4(&[
            vec![1, 2, 3, 4, 5, 6, 7, 8],
            vec![1, 2, 99, 99, 99, 99, 99, 99],
        ]);
        assert!(candidates.contains(&CandidatePair { idx1: 0, idx2: 1 }));
    }

    #[test]
    fn test_no_band_match_no_candidate() {
        // No two consecutive values match → no band match → not candidates
        let candidates = candidates_8_4(&[
            vec![1, 2, 3, 4, 5, 6, 7, 8],
            vec![1, 99, 3, 99, 5, 99, 7, 99],
        ]);
        assert!(!candidates.contains(&CandidatePair { idx1: 0, idx2: 1 }));
    }

    #[test]
    fn test_multiple_candidates_returned() {
        let config = config_with_lsh(4, 2);

        let sigs = vec![
            make_sig(vec![1, 2, 3, 4]),
            make_sig(vec![1, 2, 3, 4]),
            make_sig(vec![1, 2, 3, 4]),
        ];

        let candidates = find_candidates(&sigs, &config);

        assert!(candidates.contains(&CandidatePair { idx1: 0, idx2: 1 }));
        assert!(candidates.contains(&CandidatePair { idx1: 0, idx2: 2 }));
        assert!(candidates.contains(&CandidatePair { idx1: 1, idx2: 2 }));
    }

    #[test]
    fn test_candidate_pair_ordering() {
        let config = config_with_lsh(4, 2);

        let sigs = vec![
            make_sig(vec![1, 2, 3, 4]),
            make_sig(vec![1, 2, 3, 4]),
        ];

        let candidates = find_candidates(&sigs, &config);

        for pair in &candidates {
            assert!(pair.idx1 < pair.idx2);
        }
    }

    #[test]
    fn test_minhash_size_less_than_bands_uses_minimum() {
        let config = config_with_lsh(2, 8);

        let sigs = vec![
            make_sig(vec![1, 2]),
            make_sig(vec![1, 2]),
        ];

        let candidates = find_candidates(&sigs, &config);
        assert!(candidates.contains(&CandidatePair { idx1: 0, idx2: 1 }));
    }

    #[test]
    fn test_no_duplicate_candidates() {
        let config = config_with_lsh(4, 4);

        let sigs = vec![
            make_sig(vec![1, 1, 1, 1]),
            make_sig(vec![1, 1, 1, 1]),
        ];

        let candidates = find_candidates(&sigs, &config);

        let count = candidates
            .iter()
            .filter(|p| p.idx1 == 0 && p.idx2 == 1)
            .count();
        assert_eq!(count, 1);
    }
}
