// Allow multiple versions of transitive dependencies (getrandom 0.2 vs 0.3)
#![allow(clippy::multiple_crate_versions)]

use clap::Parser;
use std::path::PathBuf;

use dryer::config::Config;
use dryer::output;

/// Fast fuzzy duplicate detection for source code
#[derive(Parser, Debug)]
#[command(name = "dryer", version, about)]
struct Args {
    /// Directory to scan for duplicates
    path: PathBuf,

    /// Optional file paths to filter results (only report duplicates involving these files)
    filter_files: Vec<PathBuf>,

    /// File extensions to include (comma-separated, e.g., "py,rs,js")
    #[arg(short, long, default_value = "")]
    extensions: String,

    /// Minimum chunk length in characters (filters out short chunks)
    #[arg(long, default_value = "50")]
    min_chars: usize,

    /// Number of lines per chunk
    #[arg(long, default_value = "10")]
    chunk_lines: usize,

    /// Maximum normalized edit distance [0.0-1.0]
    #[arg(long, default_value = "0.15")]
    edit_threshold: f64,

    /// Character n-gram size for shingling
    #[arg(long, default_value = "5")]
    shingle_size: usize,

    /// Number of `MinHash` functions
    #[arg(long, default_value = "128")]
    minhash_size: usize,

    /// Number of LSH bands
    #[arg(long, default_value = "32")]
    lsh_bands: usize,

    /// Show the matched code strings
    #[arg(short, long)]
    verbose: bool,
}

fn main() {
    let args = Args::parse();

    let extensions: Vec<String> = if args.extensions.is_empty() {
        vec![]
    } else {
        args.extensions
            .split(',')
            .map(|s| s.trim().to_string())
            .collect()
    };

    let config = Config {
        path: args.path.clone(),
        extensions,
        min_chars: args.min_chars,
        chunk_lines: args.chunk_lines,
        edit_threshold: args.edit_threshold,
        shingle_size: args.shingle_size,
        minhash_size: args.minhash_size,
        lsh_bands: args.lsh_bands,
        filter_files: args.filter_files.clone(),
    };
    
    match dryer::run(&config) {
        Ok(result) => {
            output::print_duplicates(&result.duplicates, args.verbose, &args.path, &config.filter_files);
        }
        Err(e) => {
            eprintln!("Error: {e}");
            std::process::exit(1);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Regression test: --verbose flag should work when placed after filter files.
    /// Bug: Previously used `trailing_var_arg = true` which caused flags after
    /// filter files to be captured as additional filter file values.
    #[test]
    fn test_regression_verbose_after_filter_files() {
        // This used to fail: --verbose was captured as a filter file
        let args = Args::try_parse_from(["dryer", ".", "file1.py", "file2.py", "--verbose"])
            .expect("should parse successfully");
        
        assert!(args.verbose, "--verbose should be true when placed after filter files");
        assert_eq!(args.filter_files.len(), 2, "should have exactly 2 filter files");
        assert_eq!(args.filter_files[0], PathBuf::from("file1.py"));
        assert_eq!(args.filter_files[1], PathBuf::from("file2.py"));
    }

    #[test]
    fn test_verbose_before_filter_files() {
        let args = Args::try_parse_from(["dryer", "--verbose", ".", "file1.py"])
            .expect("should parse successfully");
        
        assert!(args.verbose);
        assert_eq!(args.filter_files.len(), 1);
    }

    #[test]
    fn test_verbose_between_path_and_filter_files() {
        let args = Args::try_parse_from(["dryer", ".", "--verbose", "file1.py"])
            .expect("should parse successfully");
        
        assert!(args.verbose);
        assert_eq!(args.filter_files.len(), 1);
    }

    #[test]
    fn test_no_filter_files() {
        let args = Args::try_parse_from(["dryer", ".", "-e", "py"])
            .expect("should parse successfully");
        
        assert!(args.filter_files.is_empty());
        assert_eq!(args.extensions, "py");
    }

    #[test]
    fn test_multiple_flags_with_filter_files() {
        let args = Args::try_parse_from([
            "dryer", "-e", "py", ".", "file.py", "--verbose", "--edit-threshold", "0.2"
        ]).expect("should parse successfully");
        
        assert!(args.verbose);
        assert_eq!(args.filter_files.len(), 1);
        assert!((args.edit_threshold - 0.2).abs() < f64::EPSILON);
    }
}
