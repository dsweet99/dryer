use crate::config::Config;
use crate::normalizer::normalize_whitespace;
use crate::scanner::SourceFile;
use rayon::prelude::*;
use std::path::PathBuf;
use std::sync::Arc;

pub type LineNumber = usize;

#[derive(Debug, Clone)]
pub struct Chunk {
    pub file: Arc<PathBuf>,
    pub start_line: LineNumber,
    pub end_line: LineNumber,
    /// Character offset from start of file
    pub file_offset: usize,
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

    // Precompute character offset for each line start
    let mut line_offsets: Vec<usize> = Vec::with_capacity(lines.len() + 1);
    let mut offset = 0;
    for line in &lines {
        line_offsets.push(offset);
        offset += line.len() + 1; // +1 for newline
    }

    let chunk_lines = config.chunk_lines;
    let overlap_step = (chunk_lines / 2).max(1);

    let mut zero_indexed_start = 0;

    while zero_indexed_start < lines.len() {
        let zero_indexed_end_exclusive = (zero_indexed_start + chunk_lines).min(lines.len());

        if zero_indexed_end_exclusive <= zero_indexed_start {
            break;
        }

        let original: String = lines[zero_indexed_start..zero_indexed_end_exclusive].join("\n");
        let normalized = normalize_whitespace(&original);

        if normalized.chars().count() >= config.min_chars {
            let one_indexed_start = zero_indexed_start + 1;
            let one_indexed_end_inclusive = zero_indexed_end_exclusive;
            let file_offset = line_offsets[zero_indexed_start];

            chunks.push(Chunk {
                file: Arc::clone(&file.path),
                start_line: one_indexed_start,
                end_line: one_indexed_end_inclusive,
                file_offset,
                original,
                normalized,
            });
        }

        zero_indexed_start += overlap_step;
    }

    chunks
}

#[cfg(test)]
mod tests {
    use super::*;

    fn test_config() -> Config {
        Config {
            min_chars: 10,  // Lower than default for short test fixtures
            chunk_lines: 10,
            ..Config::default()
        }
    }

    fn config_with_min_chars(min_chars: usize) -> Config {
        Config {
            min_chars,
            ..test_config()
        }
    }

    fn source_file(name: &str, content: &str) -> SourceFile {
        SourceFile {
            path: Arc::new(PathBuf::from(name)),
            content: content.to_string(),
        }
    }

    #[test]
    fn test_generates_chunks() {
        let file = source_file("test.py", "def foo():\n    return 42\n\ndef bar():\n    return 43\n");
        let chunks = generate_file_chunks(&file, &test_config());
        assert!(!chunks.is_empty());
    }

    #[test]
    fn test_empty_file_produces_no_chunks() {
        let file = source_file("empty.py", "");
        let chunks = generate_file_chunks(&file, &test_config());
        assert!(chunks.is_empty());
    }

    #[test]
    fn test_single_line_file() {
        let file = source_file("single.py", "x = 12345678901234567890");
        let chunks = generate_file_chunks(&file, &test_config());
        assert!(!chunks.is_empty());
        assert_eq!(chunks[0].start_line, 1);
    }

    #[test]
    fn test_chunk_line_numbers_are_1_indexed() {
        let file = source_file("test.py", "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8");
        let chunks = generate_file_chunks(&file, &config_with_min_chars(5));
        for chunk in &chunks {
            assert!(chunk.start_line >= 1, "start_line should be 1-indexed");
            assert!(chunk.end_line >= chunk.start_line);
        }
    }

    #[test]
    fn test_min_len_filters_short_chunks() {
        let file = source_file("test.py", "ab\ncd\nef");
        let chunks = generate_file_chunks(&file, &config_with_min_chars(100));
        assert!(chunks.is_empty(), "Short content should be filtered by min_len");
    }

    #[test]
    fn test_chunks_contain_original_text() {
        let file = source_file("test.py", "def foo():\n    return 42\n    # comment\n");
        let chunks = generate_file_chunks(&file, &test_config());
        assert!(!chunks.is_empty());
        assert!(chunks[0].original.contains("    return"));
    }

    #[test]
    fn test_chunks_have_normalized_text() {
        let file = source_file("test.py", "def   foo():    \n    return   42");
        let config = test_config();
        let chunks = generate_file_chunks(&file, &config);

        assert!(!chunks.is_empty());
        assert!(!chunks[0].normalized.contains("   "));
    }

    #[test]
    fn test_overlapping_chunks() {
        let lines: Vec<String> = (0..20).map(|i| format!("line number {i}")).collect();
        let file = source_file("test.py", &lines.join("\n"));
        let chunks = generate_file_chunks(&file, &test_config());
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
        let file = source_file("path/to/myfile.py", "def foo(): return 42");
        let chunks = generate_file_chunks(&file, &test_config());
        assert!(!chunks.is_empty());
        assert_eq!(*chunks[0].file, PathBuf::from("path/to/myfile.py"));
    }

    #[test]
    fn test_generate_chunks_parallel() {
        let files = vec![
            source_file("a.py", "def a(): return 'aaaaaaaaaa'"),
            source_file("b.py", "def b(): return 'bbbbbbbbbb'"),
        ];
        let chunks = generate_chunks(&files, &test_config());
        let files_seen: std::collections::HashSet<_> =
            chunks.iter().map(|c| Arc::clone(&c.file)).collect();
        assert_eq!(files_seen.len(), 2);
    }

    #[test]
    fn test_regression_end_line_semantics_match_content() {
        let file = source_file("test.py", "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10");
        let chunks = generate_file_chunks(&file, &config_with_min_chars(5));

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

    #[test]
    fn test_file_offset_first_chunk_is_zero() {
        let file = source_file("test.py", "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10");
        let chunks = generate_file_chunks(&file, &config_with_min_chars(5));
        
        assert!(!chunks.is_empty());
        assert_eq!(chunks[0].file_offset, 0, "First chunk should start at offset 0");
    }

    #[test]
    fn test_file_offset_increases_with_lines() {
        // Each line is "lineN\n" where N is 1-10
        // line1 = 5 chars + newline = 6
        // line2 starts at offset 6
        // line3 starts at offset 12, etc.
        let file = source_file("test.py", "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10");
        let config = Config {
            min_chars: 5,
            chunk_lines: 3,
            ..Config::default()
        };
        let chunks = generate_file_chunks(&file, &config);
        
        assert!(chunks.len() >= 2, "Should have at least 2 chunks");
        
        // First chunk starts at line 1 (offset 0)
        assert_eq!(chunks[0].file_offset, 0);
        assert_eq!(chunks[0].start_line, 1);
        
        // With chunk_lines=3 and overlap of 1, second chunk starts at line 2
        // "line1\n" = 6 chars, so line 2 starts at offset 6
        if chunks.len() > 1 && chunks[1].start_line == 2 {
            assert_eq!(chunks[1].file_offset, 6, "Line 2 should start at offset 6");
        }
    }

    #[test]
    fn test_file_offset_with_varying_line_lengths() {
        // Lines of different lengths
        let content = "a\nbb\nccc\ndddd\neeeee\nffffff\nggggggg\nhhhhhhhh\niiiiiiiii\njjjjjjjjjj";
        let file = source_file("test.py", content);
        let config = Config {
            min_chars: 5,
            chunk_lines: 3,
            ..Config::default()
        };
        let chunks = generate_file_chunks(&file, &config);
        
        // Line offsets: 0, 2, 5, 9, 14, 20, 27, 35, 44, 54
        // (each line length + 1 for newline, accumulated)
        if !chunks.is_empty() {
            assert_eq!(chunks[0].file_offset, 0);
        }
        
        // Find chunk starting at line 3 (offset 5: "a\n" + "bb\n" = 2 + 3 = 5)
        for chunk in &chunks {
            if chunk.start_line == 3 {
                assert_eq!(chunk.file_offset, 5, "Line 3 should start at offset 5");
            }
            if chunk.start_line == 5 {
                // "a\nbb\nccc\ndddd\n" = 2 + 3 + 4 + 5 = 14
                assert_eq!(chunk.file_offset, 14, "Line 5 should start at offset 14");
            }
        }
    }
}
