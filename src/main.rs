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
        path: args.path,
        extensions,
        min_chars: args.min_chars,
        chunk_lines: args.chunk_lines,
        edit_threshold: args.edit_threshold,
        shingle_size: args.shingle_size,
        minhash_size: args.minhash_size,
        lsh_bands: args.lsh_bands,
    };
    
    match dryer::run(&config) {
        Ok(result) => {
            output::print_duplicates(&result.duplicates, args.verbose);
        }
        Err(e) => {
            eprintln!("Error: {e}");
            std::process::exit(1);
        }
    }
}
