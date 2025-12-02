//! Generates a synthetic codebase for benchmarking.
//!
//! Run with: `cargo run --release --example generate_benchmark_data`
//!
//! Creates `tests/benchmark_data/` with Python files.

use std::fs;
use std::io::Write;
use std::path::Path;

fn main() {
    let output_dir = Path::new("../tests/benchmark_data");
    
    if output_dir.exists() {
        fs::remove_dir_all(output_dir).expect("Failed to remove existing directory");
    }
    fs::create_dir_all(output_dir).expect("Failed to create directory");

    let mut total_files = 0;
    let mut total_functions = 0;

    // 30 files, 20 functions each = 600 functions
    // ~80% unique, ~20% duplicates
    for file_id in 0..30 {
        let file_path = output_dir.join(format!("module_{file_id:03}.py"));
        let mut file = fs::File::create(&file_path).expect("Failed to create file");

        writeln!(file, "\"\"\"Module {file_id}\"\"\"").unwrap();
        writeln!(file).unwrap();

        for func_id in 0..20 {
            let func = generate_function(file_id, func_id);
            writeln!(file, "{func}").unwrap();
            total_functions += 1;
        }

        total_files += 1;
    }

    println!("Generated: {total_files} files, {total_functions} functions");
    println!("Run: cargo run --release --example timing ../tests/benchmark_data");
}

fn generate_function(file_id: usize, func_id: usize) -> String {
    // 80% unique, 20% duplicates
    if func_id < 16 {
        generate_unique(file_id, func_id)
    } else {
        generate_duplicate(func_id)
    }
}

fn generate_unique(file_id: usize, func_id: usize) -> String {
    let v1 = file_id * 17 + func_id * 3 + 1;
    let v2 = file_id * 13 + func_id * 7 + 2;
    let v3 = file_id * 11 + func_id * 5 + 3;
    let v4 = file_id * 7 + func_id * 11 + 4;
    let v5 = (file_id + func_id) % 20 + 5;
    let v6 = file_id * 3 + func_id + 1;
    let v7 = file_id + func_id * 2 + 1;
    let v8 = 5000 + file_id * 100 + func_id * 10;
    let v9 = 1000 + file_id * 50 + func_id * 5;
    let v10 = file_id * func_id + 1;
    format!(
r"def compute_{file_id}_{func_id}(a, b, c):
    x = a * {v1} + b * {v2}
    y = c * {v3} - a * {v4}
    for i in range({v5}):
        x = x + i * {v6}
        y = y - i * {v7}
        if x > {v8}:
            x = x % {v9}
    return x + y + {v10}

"
    )
}

fn generate_duplicate(func_id: usize) -> String {
    // Same across all files - creates duplicates
    format!(
r#"def shared_util_{func_id}(data):
    if data is None:
        raise ValueError("data required")
    result = []
    for item in data:
        if item is not None:
            val = str(item).strip()
            if len(val) > 0:
                result.append(val)
    return result

"#
    )
}
