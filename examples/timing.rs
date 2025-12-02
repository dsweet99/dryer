//! Timing benchmark for dryer duplicate detection pipeline.
//!
//! Run with: cargo run --release --example timing
//!
//! This measures the time taken by each phase of the pipeline:
//! 1. File scanning
//! 2. Chunk generation
//! 3. `MinHash` signature computation
//! 4. LSH candidate generation
//! 5. Edit distance verification

use dryer::chunker;
use dryer::config::Config;
use dryer::edit_distance;
use dryer::lsh;
use dryer::minhash;
use dryer::scanner;
use std::path::PathBuf;
use std::time::{Duration, Instant};

const BENCHMARK_RUNS: usize = 5;
const ITERATIONS_PER_RUN: usize = 3;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    
    let path = if args.len() > 1 {
        PathBuf::from(&args[1])
    } else {
        PathBuf::from("../tests/fake_code")
    };

    let config = Config {
        path: path.clone(),
        extensions: vec!["py".to_string()],
        min_len: 10,
        max_len: 500,
        edit_threshold: 0.15,
        shingle_size: 5,
        minhash_size: 128,
        lsh_bands: 32,
        json_output: false,
    };

    println!("=== Dryer Timing Benchmark ===");
    println!("Path: {}", path.display());
    println!("Config: min_len={}, max_len={}, threshold={}", 
             config.min_len, config.max_len, config.edit_threshold);
    println!();

    // Warm-up run
    println!("Warming up...");
    let _ = dryer::run(&config);
    println!();

    println!("Running {BENCHMARK_RUNS} benchmark runs ({ITERATIONS_PER_RUN} iterations each)...");
    println!();

    let mut run_results: Vec<RunResult> = Vec::with_capacity(BENCHMARK_RUNS);

    for run in 0..BENCHMARK_RUNS {
        let result = benchmark_run(&config);
        println!("Run {}: {:.1} ms ({} candidates, {} duplicates)", 
                 run + 1, 
                 result.total_ms,
                 result.candidates,
                 result.duplicates);
        run_results.push(result);
    }

    println!();
    println!("=== Results ({BENCHMARK_RUNS} runs) ===");
    println!();

    // Calculate and print statistics
    print_stats("File scanning", &run_results, |r| r.scanning_ms);
    print_stats("Chunk generation", &run_results, |r| r.chunking_ms);
    print_stats("MinHash signatures", &run_results, |r| r.minhash_ms);
    print_stats("LSH candidates", &run_results, |r| r.lsh_ms);
    print_stats("Edit distance", &run_results, |r| r.verification_ms);
    println!("{:-<60}", "");
    print_stats("TOTAL", &run_results, |r| r.total_ms);
    
    println!();
    #[allow(clippy::cast_precision_loss)]
    let candidates: Vec<f64> = run_results.iter().map(|r| r.candidates as f64).collect();
    #[allow(clippy::cast_precision_loss)]
    let duplicates: Vec<f64> = run_results.iter().map(|r| r.duplicates as f64).collect();
    println!("Candidates: {:.0} ± {:.0}", mean(&candidates), std_error(&candidates));
    println!("Duplicates: {:.0} ± {:.0}", mean(&duplicates), std_error(&duplicates));
}

struct RunResult {
    scanning_ms: f64,
    chunking_ms: f64,
    minhash_ms: f64,
    lsh_ms: f64,
    verification_ms: f64,
    total_ms: f64,
    candidates: usize,
    duplicates: usize,
}

fn benchmark_run(config: &Config) -> RunResult {
    let mut scanning_times = Vec::with_capacity(ITERATIONS_PER_RUN);
    let mut chunking_times = Vec::with_capacity(ITERATIONS_PER_RUN);
    let mut minhash_times = Vec::with_capacity(ITERATIONS_PER_RUN);
    let mut lsh_times = Vec::with_capacity(ITERATIONS_PER_RUN);
    let mut verification_times = Vec::with_capacity(ITERATIONS_PER_RUN);
    let mut total_times = Vec::with_capacity(ITERATIONS_PER_RUN);
    
    let mut last_candidates = 0;
    let mut last_duplicates = 0;

    for _ in 0..ITERATIONS_PER_RUN {
        let iter_start = Instant::now();

        let start = Instant::now();
        let files = scanner::scan_files(&config.path, &config.extensions)
            .expect("scan failed");
        scanning_times.push(start.elapsed());

        let start = Instant::now();
        let chunks = chunker::generate_chunks(&files, config);
        chunking_times.push(start.elapsed());

        let start = Instant::now();
        let signatures = minhash::compute_signatures(&chunks, config);
        minhash_times.push(start.elapsed());

        let start = Instant::now();
        let candidates = lsh::find_candidates(&signatures, config);
        lsh_times.push(start.elapsed());
        last_candidates = candidates.len();

        let start = Instant::now();
        let duplicates = edit_distance::verify_candidates(&chunks, &signatures, &candidates, config);
        verification_times.push(start.elapsed());
        last_duplicates = duplicates.len();

        total_times.push(iter_start.elapsed());
    }

    RunResult {
        scanning_ms: median_ms(&scanning_times),
        chunking_ms: median_ms(&chunking_times),
        minhash_ms: median_ms(&minhash_times),
        lsh_ms: median_ms(&lsh_times),
        verification_ms: median_ms(&verification_times),
        total_ms: median_ms(&total_times),
        candidates: last_candidates,
        duplicates: last_duplicates,
    }
}

fn median_ms(times: &[Duration]) -> f64 {
    let mut sorted: Vec<Duration> = times.to_vec();
    sorted.sort();
    sorted[sorted.len() / 2].as_secs_f64() * 1000.0
}

#[allow(clippy::cast_precision_loss)]
fn mean(values: &[f64]) -> f64 {
    values.iter().sum::<f64>() / values.len() as f64
}

#[allow(clippy::cast_precision_loss)]
fn std_dev(values: &[f64]) -> f64 {
    let m = mean(values);
    let variance = values.iter().map(|x| (x - m).powi(2)).sum::<f64>() / values.len() as f64;
    variance.sqrt()
}

#[allow(clippy::cast_precision_loss)]
fn std_error(values: &[f64]) -> f64 {
    std_dev(values) / (values.len() as f64).sqrt()
}

fn print_stats<F>(name: &str, results: &[RunResult], extractor: F)
where
    F: Fn(&RunResult) -> f64,
{
    let values: Vec<f64> = results.iter().map(&extractor).collect();
    let m = mean(&values);
    let se = std_error(&values);
    println!("{name:<22} {m:>8.1} ± {se:>5.1} ms");
}
