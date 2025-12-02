use crate::config::Config;
use crate::normalizer::normalize_whitespace;
use crate::scanner::SourceFile;
use rayon::prelude::*;
use std::path::PathBuf;
use std::sync::Arc;

pub type LineNumber = usize;

const AVERAGE_CHARS_PER_LINE: usize = 40;
const MIN_LINES_PER_CHUNK: usize = 3;
const CHUNK_SIZE_DIVISOR: usize = 2;

#[derive(Debug, Clone)]
pub struct Chunk {
    pub file: Arc<PathBuf>,
    pub start_line: LineNumber,
    pub end_line: LineNumber,
    pub original: String,
    pub normalized: String,
}

pub fn generate_chunks(files: &[SourceFile], config: &Config) -> Vec<Chunk> {
    files
        .par_iter()
        .flat_map(|file| generate_file_chunks(file, config))
        .collect()
}

fn generate_file_chunks(file: &SourceFile, config: &Config) -> Vec<Chunk> {
    let mut chunks = Vec::new();
    let lines: Vec<&str> = file.content.lines().collect();

    if lines.is_empty() {
        return chunks;
    }

    let target_lines = estimate_lines_for_chars(config.max_len / CHUNK_SIZE_DIVISOR);
    let overlap_step = (target_lines / CHUNK_SIZE_DIVISOR).max(1);

    let mut zero_indexed_start = 0;

    while zero_indexed_start < lines.len() {
        let zero_indexed_end_exclusive = (zero_indexed_start + target_lines).min(lines.len());

        if zero_indexed_end_exclusive <= zero_indexed_start {
            break;
        }

        let original: String = lines[zero_indexed_start..zero_indexed_end_exclusive].join("\n");
        let normalized = normalize_whitespace(&original);

        if normalized.chars().count() >= config.min_len {
            let one_indexed_start = zero_indexed_start + 1;
            let one_indexed_end_inclusive = zero_indexed_end_exclusive;

            chunks.push(Chunk {
                file: Arc::clone(&file.path),
                start_line: one_indexed_start,
                end_line: one_indexed_end_inclusive,
                original,
                normalized,
            });
        }

        zero_indexed_start += overlap_step;
    }

    chunks
}

fn estimate_lines_for_chars(chars: usize) -> usize {
    (chars / AVERAGE_CHARS_PER_LINE).max(MIN_LINES_PER_CHUNK)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn test_config() -> Config {
        Config {
            min_len: 10,  // Lower than default for short test fixtures
            max_len: 100,
            ..Config::default()
        }
    }

    fn config_with_min_len(min_len: usize) -> Config {
        Config {
            min_len,
            ..test_config()
        }
    }

    #[test]
    fn test_generates_chunks() {
        let file = SourceFile {
            path: Arc::new(PathBuf::from("test.py")),
            content: "def foo():\n    return 42\n\ndef bar():\n    return 43\n".to_string(),
        };
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);
        assert!(!chunks.is_empty());
    }

    #[test]
    fn test_empty_file_produces_no_chunks() {
        let file = SourceFile {
            path: Arc::new(PathBuf::from("empty.py")),
            content: String::new(),
        };
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);
        assert!(chunks.is_empty());
    }

    #[test]
    fn test_single_line_file() {
        let file = SourceFile {
            path: Arc::new(PathBuf::from("single.py")),
            content: "x = 12345678901234567890".to_string(),
        };
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);
        assert!(!chunks.is_empty());
        assert_eq!(chunks[0].start_line, 1);
    }

    #[test]
    fn test_chunk_line_numbers_are_1_indexed() {
        let file = SourceFile {
            path: Arc::new(PathBuf::from("test.py")),
            content: "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8".to_string(),
        };
        let config = config_with_min_len(5);
        let chunks = generate_file_chunks(&file, &config);

        for chunk in &chunks {
            assert!(chunk.start_line >= 1, "start_line should be 1-indexed");
            assert!(chunk.end_line >= chunk.start_line);
        }
    }

    #[test]
    fn test_min_len_filters_short_chunks() {
        let file = SourceFile {
            path: Arc::new(PathBuf::from("test.py")),
            content: "ab\ncd\nef".to_string(),
        };
        let config = config_with_min_len(100);
        let chunks = generate_file_chunks(&file, &config);
        assert!(chunks.is_empty(), "Short content should be filtered by min_len");
    }

    #[test]
    fn test_chunks_contain_original_text() {
        let content = "def foo():\n    return 42\n    # comment\n".to_string();
        let file = SourceFile {
            path: Arc::new(PathBuf::from("test.py")),
            content,
        };
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);

        assert!(!chunks.is_empty());
        assert!(chunks[0].original.contains("    return"));
    }

    #[test]
    fn test_chunks_have_normalized_text() {
        let file = SourceFile {
            path: Arc::new(PathBuf::from("test.py")),
            content: "def   foo():    \n    return   42".to_string(),
        };
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);

        assert!(!chunks.is_empty());
        assert!(!chunks[0].normalized.contains("   "));
    }

    #[test]
    fn test_overlapping_chunks() {
        let lines: Vec<String> = (0..20).map(|i| format!("line number {i}")).collect();
        let content = lines.join("\n");
        let file = SourceFile {
            path: Arc::new(PathBuf::from("test.py")),
            content,
        };
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);

        if chunks.len() >= 2 {
            let first_end = chunks[0].end_line;
            let second_start = chunks[1].start_line;
            assert!(
                second_start < first_end,
                "Chunks should overlap: first ends at {first_end}, second starts at {second_start}"
            );
        }
    }

    #[test]
    fn test_chunk_preserves_file_path() {
        let file = SourceFile {
            path: Arc::new(PathBuf::from("path/to/myfile.py")),
            content: "def foo(): return 42".to_string(),
        };
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);

        assert!(!chunks.is_empty());
        assert_eq!(*chunks[0].file, PathBuf::from("path/to/myfile.py"));
    }

    #[test]
    fn test_generate_chunks_parallel() {
        let files = vec![
            SourceFile {
                path: Arc::new(PathBuf::from("a.py")),
                content: "def a(): return 'aaaaaaaaaa'".to_string(),
            },
            SourceFile {
                path: Arc::new(PathBuf::from("b.py")),
                content: "def b(): return 'bbbbbbbbbb'".to_string(),
            },
        ];
        let config = test_config();
        let chunks = generate_chunks(&files, &config);

        let files_seen: std::collections::HashSet<_> =
            chunks.iter().map(|c| Arc::clone(&c.file)).collect();
        assert_eq!(files_seen.len(), 2);
    }

    #[test]
    fn test_regression_end_line_semantics_match_content() {
        let content = "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10";
        let file = SourceFile {
            path: Arc::new(PathBuf::from("test.py")),
            content: content.to_string(),
        };
        let config = config_with_min_len(5);
        let chunks = generate_file_chunks(&file, &config);

        for chunk in &chunks {
            let actual_line_count = chunk.original.lines().count();
            let expected_line_count = chunk.end_line - chunk.start_line + 1;

            assert_eq!(
                actual_line_count, expected_line_count,
                "Chunk lines {}-{}: expected {} lines but found {} in content: {:?}",
                chunk.start_line, chunk.end_line, expected_line_count, actual_line_count, chunk.original
            );

            let first_line = chunk.original.lines().next().unwrap_or("");
            let expected_first = format!("line{}", chunk.start_line);
            assert!(
                first_line.contains(&expected_first),
                "Chunk starting at line {} should contain '{}', got '{}'",
                chunk.start_line, expected_first, first_line
            );
        }
    }
}
