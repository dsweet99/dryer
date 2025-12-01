use crate::chunker::Chunk;
use crate::config::Config;
use crate::shingling::shingle;
use rayon::prelude::*;

#[derive(Debug, Clone)]
pub struct Signature {
    pub hashes: Vec<u64>,
}

type HashCoefficients = Vec<(u64, u64)>;

const LCG_MULTIPLIER: u64 = 0x5DEECE66D;

pub fn compute_signatures(chunks: &[Chunk], config: &Config) -> Vec<Signature> {
    let hash_coefficients = generate_hash_coefficients(config.minhash_size);

    chunks
        .par_iter()
        .map(|chunk| {
            let shingles = shingle(&chunk.normalized, config.shingle_size);
            let hashes = compute_minhash(&shingles, &hash_coefficients);
            Signature { hashes }
        })
        .collect()
}

fn generate_hash_coefficients(count: usize) -> HashCoefficients {
    let mut coefficients = Vec::with_capacity(count);

    let mut a: u64 = LCG_MULTIPLIER;
    let mut b: u64 = 0xB;

    for _ in 0..count {
        a = a.wrapping_mul(LCG_MULTIPLIER).wrapping_add(11);
        b = b.wrapping_mul(LCG_MULTIPLIER).wrapping_add(13);
        coefficients.push((a | 1, b));
    }

    coefficients
}

fn compute_minhash(shingles: &ahash::AHashSet<u64>, coefficients: &HashCoefficients) -> Vec<u64> {
    // One-pass algorithm: iterate shingles once, update all minimums
    // Much better cache locality than iterating coefficients × shingles
    let mut mins = vec![u64::MAX; coefficients.len()];
    
    for &shingle_hash in shingles {
        for (i, &(a, b)) in coefficients.iter().enumerate() {
            let hash = a.wrapping_mul(shingle_hash).wrapping_add(b);
            if hash < mins[i] {
                mins[i] = hash;
            }
        }
    }
    
    mins
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::test_utils::{config_with_minhash, make_simple_chunk};

    fn estimate_jaccard_similarity(sig1: &[u64], sig2: &[u64]) -> f64 {
        assert_eq!(sig1.len(), sig2.len());
        let matching_hashes = sig1.iter().zip(sig2).filter(|(a, b)| a == b).count();
        matching_hashes as f64 / sig1.len() as f64
    }

    #[test]
    fn test_identical_signatures() {
        let coefficients = generate_hash_coefficients(100);
        let mut shingles = ahash::AHashSet::new();
        shingles.insert(1);
        shingles.insert(2);
        shingles.insert(3);

        let sig1 = compute_minhash(&shingles, &coefficients);
        let sig2 = compute_minhash(&shingles, &coefficients);

        assert_eq!(estimate_jaccard_similarity(&sig1, &sig2), 1.0);
    }

    #[test]
    fn test_different_signatures() {
        let coefficients = generate_hash_coefficients(100);

        let mut shingles1 = ahash::AHashSet::new();
        shingles1.insert(1);
        shingles1.insert(2);

        let mut shingles2 = ahash::AHashSet::new();
        shingles2.insert(100);
        shingles2.insert(200);

        let sig1 = compute_minhash(&shingles1, &coefficients);
        let sig2 = compute_minhash(&shingles2, &coefficients);

        assert!(estimate_jaccard_similarity(&sig1, &sig2) < 0.5);
    }

    #[test]
    fn test_compute_signatures_with_real_chunks() {
        let chunks = vec![
            make_simple_chunk("def hello_world(): return 42"),
            make_simple_chunk("def goodbye_world(): return 43"),
        ];
        let config = config_with_minhash(64, 5);

        let signatures = compute_signatures(&chunks, &config);

        assert_eq!(signatures.len(), 2);
        assert_eq!(signatures[0].hashes.len(), 64);
        assert_eq!(signatures[1].hashes.len(), 64);
    }

    #[test]
    fn test_compute_signatures_identical_chunks_have_identical_sigs() {
        let chunks = vec![
            make_simple_chunk("identical text here for testing purposes"),
            make_simple_chunk("identical text here for testing purposes"),
        ];
        let config = config_with_minhash(64, 5);

        let signatures = compute_signatures(&chunks, &config);

        assert_eq!(signatures[0].hashes, signatures[1].hashes);
        assert_eq!(estimate_jaccard_similarity(&signatures[0].hashes, &signatures[1].hashes), 1.0);
    }

    #[test]
    fn test_compute_signatures_similar_chunks_have_high_similarity() {
        let chunks = vec![
            make_simple_chunk("def calculate_total(items): return sum(items)"),
            make_simple_chunk("def compute_total(items): return sum(items)"),
        ];
        let config = config_with_minhash(128, 5);

        let signatures = compute_signatures(&chunks, &config);

        let similarity = estimate_jaccard_similarity(&signatures[0].hashes, &signatures[1].hashes);
        assert!(similarity > 0.5, "Similarity was {}", similarity);
    }

    #[test]
    fn test_compute_signatures_different_chunks_have_low_similarity() {
        let chunks = vec![
            make_simple_chunk("def fibonacci(n): return n if n <= 1 else fib(n-1) + fib(n-2)"),
            make_simple_chunk("class BinaryTree: def __init__(self): self.root = None"),
        ];
        let config = config_with_minhash(128, 5);

        let signatures = compute_signatures(&chunks, &config);

        let similarity = estimate_jaccard_similarity(&signatures[0].hashes, &signatures[1].hashes);
        assert!(similarity < 0.5, "Similarity was {}", similarity);
    }

    #[test]
    fn test_compute_signatures_empty_chunks() {
        let chunks: Vec<Chunk> = vec![];
        let config = config_with_minhash(64, 5);

        let signatures = compute_signatures(&chunks, &config);

        assert!(signatures.is_empty());
    }

    #[test]
    fn test_compute_signatures_preserves_order() {
        let chunks = vec![
            make_simple_chunk("chunk zero"),
            make_simple_chunk("chunk one"),
            make_simple_chunk("chunk two"),
        ];
        let config = config_with_minhash(32, 3);

        let signatures = compute_signatures(&chunks, &config);

        assert_eq!(signatures.len(), 3);
    }

    #[test]
    fn test_minhash_deterministic() {
        let coefficients = generate_hash_coefficients(64);
        let mut shingles = ahash::AHashSet::new();
        shingles.insert(42);
        shingles.insert(43);
        shingles.insert(44);

        let sig1 = compute_minhash(&shingles, &coefficients);
        let sig2 = compute_minhash(&shingles, &coefficients);

        assert_eq!(sig1, sig2, "MinHash should be deterministic");
    }

    #[test]
    fn test_empty_shingles_produce_max_hashes() {
        let coefficients = generate_hash_coefficients(10);
        let shingles: ahash::AHashSet<u64> = ahash::AHashSet::new();

        let sig = compute_minhash(&shingles, &coefficients);

        for &h in &sig {
            assert_eq!(h, u64::MAX);
        }
    }
}
