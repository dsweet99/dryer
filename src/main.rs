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

    /// Minimum chunk length in characters
    #[arg(long, default_value = "10")]
    min_len: usize,

    /// Maximum chunk length in characters
    #[arg(long, default_value = "500")]
    max_len: usize,

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

    /// Output as JSON instead of diff
    #[arg(long, default_value = "false")]
    json: bool,
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
        min_len: args.min_len,
        max_len: args.max_len,
        edit_threshold: args.edit_threshold,
        shingle_size: args.shingle_size,
        minhash_size: args.minhash_size,
        lsh_bands: args.lsh_bands,
        json_output: args.json,
    };

    let json_output = config.json_output;
    
    match dryer::run(&config) {
        Ok(duplicates) => {
            if json_output {
                if let Err(e) = output::print_json(&duplicates) {
                    eprintln!("Error: {e}");
                    std::process::exit(1);
                }
            } else {
                output::print_diff(&duplicates);
            }
        }
        Err(e) => {
            eprintln!("Error: {e}");
            std::process::exit(1);
        }
    }
}
