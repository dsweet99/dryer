use crate::edit_distance::Duplicate;
use serde::Serialize;
use std::io::{self, BufWriter, Write};

const HEADER_WIDTH: usize = 70;

#[derive(Serialize)]
struct JsonDuplicate {
    file1: String,
    start_line1: usize,
    end_line1: usize,
    file2: String,
    start_line2: usize,
    end_line2: usize,
    edit_distance: usize,
    normalized_distance: f64,
    text1: String,
    text2: String,
}

pub fn print_json(duplicates: &[Duplicate]) -> io::Result<()> {
    let json_dupes: Vec<JsonDuplicate> = duplicates
        .iter()
        .map(|d| JsonDuplicate {
            file1: d.chunk1.file.display().to_string(),
            start_line1: d.chunk1.start_line,
            end_line1: d.chunk1.end_line,
            file2: d.chunk2.file.display().to_string(),
            start_line2: d.chunk2.start_line,
            end_line2: d.chunk2.end_line,
            edit_distance: d.edit_distance,
            normalized_distance: d.normalized_distance,
            text1: d.chunk1.original.clone(),
            text2: d.chunk2.original.clone(),
        })
        .collect();

    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());
    serde_json::to_writer_pretty(&mut out, &json_dupes)?;
    writeln!(out)?;
    Ok(())
}

pub fn print_diff(duplicates: &[Duplicate]) {
    let stdout = io::stdout();
    let mut out = stdout.lock();

    for (i, dup) in duplicates.iter().enumerate() {
        if i > 0 {
            writeln!(out).unwrap();
        }

        print_duplicate_header(&mut out, i + 1, dup.normalized_distance);
        print_file_locations(&mut out, dup);
        print_chunk_diff(&mut out, dup);
    }

    print_summary(&mut out, duplicates.len());
}

fn print_duplicate_header(out: &mut impl Write, number: usize, normalized_distance: f64) {
    writeln!(out, "{}", "=".repeat(HEADER_WIDTH)).unwrap();
    writeln!(out, "Duplicate #{} (distance: {:.1}%)", number, normalized_distance * 100.0).unwrap();
    writeln!(out, "{}", "=".repeat(HEADER_WIDTH)).unwrap();
}

fn print_file_locations(out: &mut impl Write, dup: &Duplicate) {
    writeln!(
        out,
        "--- {}:{}-{}",
        dup.chunk1.file.display(),
        dup.chunk1.start_line,
        dup.chunk1.end_line
    ).unwrap();

    writeln!(
        out,
        "+++ {}:{}-{}",
        dup.chunk2.file.display(),
        dup.chunk2.start_line,
        dup.chunk2.end_line
    ).unwrap();

    writeln!(out).unwrap();
}

fn print_chunk_diff(out: &mut impl Write, dup: &Duplicate) {
    for line in dup.chunk1.original.lines() {
        writeln!(out, "- {}", line).unwrap();
    }

    writeln!(out).unwrap();

    for line in dup.chunk2.original.lines() {
        writeln!(out, "+ {}", line).unwrap();
    }
}

fn print_summary(out: &mut impl Write, count: usize) {
    if count == 0 {
        writeln!(out, "No duplicates found.").unwrap();
    } else {
        writeln!(out).unwrap();
        writeln!(out, "Found {} duplicate(s)", count).unwrap();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::chunker::Chunk;
    use crate::test_utils::make_chunk;

    fn make_duplicate(c1: Chunk, c2: Chunk, dist: usize, norm: f64) -> Duplicate {
        Duplicate {
            chunk1: c1,
            chunk2: c2,
            edit_distance: dist,
            normalized_distance: norm,
        }
    }

    fn to_json_duplicate(d: &Duplicate) -> JsonDuplicate {
        JsonDuplicate {
            file1: d.chunk1.file.display().to_string(),
            start_line1: d.chunk1.start_line,
            end_line1: d.chunk1.end_line,
            file2: d.chunk2.file.display().to_string(),
            start_line2: d.chunk2.start_line,
            end_line2: d.chunk2.end_line,
            edit_distance: d.edit_distance,
            normalized_distance: d.normalized_distance,
            text1: d.chunk1.original.clone(),
            text2: d.chunk2.original.clone(),
        }
    }

    fn to_json_duplicates(duplicates: &[Duplicate]) -> Vec<JsonDuplicate> {
        duplicates.iter().map(to_json_duplicate).collect()
    }

    #[test]
    fn test_json_output() {
        let dup = make_duplicate(
            make_chunk("a.py", 1, 5, "hello"),
            make_chunk("b.py", 10, 15, "hallo"),
            1,
            0.2,
        );

        let json_dupes = to_json_duplicates(&[dup]);
        let json = serde_json::to_string_pretty(&json_dupes).unwrap();
        assert!(json.contains("a.py"));
    }

    #[test]
    fn test_json_output_contains_all_fields() {
        let dup = make_duplicate(
            make_chunk("src/foo.py", 10, 20, "def foo(): pass"),
            make_chunk("src/bar.py", 30, 40, "def bar(): pass"),
            5,
            0.15,
        );

        let json_dup = to_json_duplicate(&dup);
        let json = serde_json::to_string(&json_dup).unwrap();

        assert!(json.contains("\"file1\":"));
        assert!(json.contains("\"file2\":"));
        assert!(json.contains("\"start_line1\":10"));
        assert!(json.contains("\"end_line1\":20"));
        assert!(json.contains("\"start_line2\":30"));
        assert!(json.contains("\"end_line2\":40"));
        assert!(json.contains("\"edit_distance\":5"));
        assert!(json.contains("\"normalized_distance\":0.15"));
        assert!(json.contains("\"text1\":"));
        assert!(json.contains("\"text2\":"));
    }

    #[test]
    fn test_json_empty_duplicates() {
        let duplicates: Vec<Duplicate> = vec![];
        let json_dupes = to_json_duplicates(&duplicates);
        let json = serde_json::to_string_pretty(&json_dupes).unwrap();
        assert_eq!(json, "[]");
    }

    #[test]
    fn test_json_multiple_duplicates() {
        let duplicates = vec![
            make_duplicate(
                make_chunk("a.py", 1, 5, "code1"),
                make_chunk("b.py", 1, 5, "code2"),
                1,
                0.1,
            ),
            make_duplicate(
                make_chunk("c.py", 10, 15, "code3"),
                make_chunk("d.py", 20, 25, "code4"),
                2,
                0.2,
            ),
        ];

        let json_dupes = to_json_duplicates(&duplicates);
        let json = serde_json::to_string_pretty(&json_dupes).unwrap();
        assert!(json.contains("a.py"));
        assert!(json.contains("c.py"));
        assert!(json.contains("d.py"));
    }

    #[test]
    fn test_json_escapes_special_characters() {
        let dup = make_duplicate(
            make_chunk("test.py", 1, 2, "print(\"hello\\nworld\")"),
            make_chunk("test2.py", 1, 2, "print('hello\\nworld')"),
            2,
            0.1,
        );

        let json_dup = to_json_duplicate(&dup);
        let json = serde_json::to_string(&json_dup).unwrap();
        let _: serde_json::Value = serde_json::from_str(&json).unwrap();
    }
}
