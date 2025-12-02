use crate::edit_distance::Duplicate;
use std::io::{self, Write};

/// Print duplicates in compact one-line-per-match format
pub fn print_markdown(duplicates: &[Duplicate], _total_files: usize, _total_chunks: usize) {
    let stdout = io::stdout();
    let mut out = stdout.lock();

    for dup in duplicates {
        writeln!(
            out,
            "{:.1}% {}:{}-{} {}:{}-{}",
            dup.normalized_distance * 100.0,
            dup.chunk1.file.display(),
            dup.chunk1.start_line,
            dup.chunk1.end_line,
            dup.chunk2.file.display(),
            dup.chunk2.start_line,
            dup.chunk2.end_line
        )
        .unwrap();
    }
}

