use ahash::AHashSet;

pub fn shingle(text: &str, ngram_size: usize) -> AHashSet<u64> {
    let chars: Vec<char> = text.chars().collect();
    let mut shingles = AHashSet::new();

    if chars.len() < ngram_size {
        shingles.insert(hash_char_slice(&chars));
        return shingles;
    }

    for window in chars.windows(ngram_size) {
        shingles.insert(hash_char_slice(window));
    }

    shingles
}

fn hash_char_slice(chars: &[char]) -> u64 {
    use std::hash::{Hash, Hasher};
    let mut hasher = ahash::AHasher::default();
    chars.hash(&mut hasher);
    hasher.finish()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_shingle_basic() {
        let shingles = shingle("hello", 3);
        assert_eq!(shingles.len(), 3);
    }

    #[test]
    fn test_shingle_short_text() {
        let shingles = shingle("hi", 5);
        assert_eq!(shingles.len(), 1);
    }

    #[test]
    fn test_similar_strings_share_shingles() {
        let s1 = shingle("hello world", 3);
        let s2 = shingle("hello there", 3);

        let shared = s1.intersection(&s2).count();
        assert!(shared > 0);
    }
}
