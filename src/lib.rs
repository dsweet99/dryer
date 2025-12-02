pub mod chunker;
pub mod config;
pub mod edit_distance;
pub mod lsh;
pub mod minhash;
pub mod normalizer;
pub mod output;
pub mod scanner;
pub mod shingling;

use config::Config;

/// Result of running duplicate detection
pub struct RunResult {
    pub duplicates: Vec<edit_distance::Duplicate>,
    pub file_count: usize,
    pub chunk_count: usize,
}

pub fn run(config: &Config) -> Result<RunResult, Box<dyn std::error::Error>> {
    config.validate()?;

    let files = scanner::scan_files(&config.path, &config.extensions)?;
    let file_count = files.len();
    eprintln!("Found {file_count} files");

    let chunks = chunker::generate_chunks(&files, config);
    let chunk_count = chunks.len();
    eprintln!("Generated {chunk_count} chunks");

    if chunks.is_empty() {
        eprintln!("No chunks to analyze");
        return Ok(RunResult {
            duplicates: vec![],
            file_count,
            chunk_count,
        });
    }

    let signatures = minhash::compute_signatures(&chunks, config);
    eprintln!("Computed {} signatures", signatures.len());

    let candidates = lsh::find_candidates(&signatures, config);
    eprintln!("Found {} candidate pairs", candidates.len());

    let duplicates = edit_distance::verify_candidates(&chunks, &signatures, &candidates, config);
    eprintln!("Verified {} duplicates", duplicates.len());

    Ok(RunResult {
        duplicates,
        file_count,
        chunk_count,
    })
}

#[cfg(test)]
pub mod test_utils {
    use crate::chunker::Chunk;
    use crate::config::Config;
    use std::path::PathBuf;
    use std::sync::Arc;

    pub fn make_chunk(file: &str, start: usize, end: usize, text: &str) -> Chunk {
        Chunk {
            file: Arc::new(PathBuf::from(file)),
            start_line: start,
            end_line: end,
            original: text.to_string(),
            normalized: text.to_string(),
        }
    }

    pub fn make_simple_chunk(text: &str) -> Chunk {
        make_chunk("test.py", 1, 5, text)
    }

    pub fn config_with_minhash(minhash_size: usize, shingle_size: usize) -> Config {
        Config {
            shingle_size,
            minhash_size,
            ..Config::default()
        }
    }

    pub fn config_with_lsh(minhash_size: usize, lsh_bands: usize) -> Config {
        Config {
            minhash_size,
            lsh_bands,
            ..Config::default()
        }
    }

    pub fn config_with_threshold(threshold: f64) -> Config {
        Config {
            edit_threshold: threshold,
            ..Config::default()
        }
    }
}
