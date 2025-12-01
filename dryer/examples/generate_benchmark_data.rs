//! Generates a synthetic codebase for benchmarking.
//!
//! Run with: cargo run --release --example generate_benchmark_data
//!
//! Creates test/benchmark_data/ with Python files.

use std::fs;
use std::io::Write;
use std::path::Path;

fn main() {
    let output_dir = Path::new("../test/benchmark_data");
    
    if output_dir.exists() {
        fs::remove_dir_all(output_dir).expect("Failed to remove existing directory");
    }
    fs::create_dir_all(output_dir).expect("Failed to create directory");

    let mut total_files = 0;
    let mut total_functions = 0;

    // 30 files, 20 functions each = 600 functions
    // ~80% unique, ~20% duplicates
    for file_id in 0..30 {
        let file_path = output_dir.join(format!("module_{:03}.py", file_id));
        let mut file = fs::File::create(&file_path).expect("Failed to create file");

        writeln!(file, "\"\"\"Module {}\"\"\"", file_id).unwrap();
        writeln!(file).unwrap();

        for func_id in 0..20 {
            let func = generate_function(file_id, func_id);
            writeln!(file, "{}", func).unwrap();
            total_functions += 1;
        }

        total_files += 1;
    }

    println!("Generated: {} files, {} functions", total_files, total_functions);
    println!("Run: cargo run --release --example timing ../test/benchmark_data");
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
    format!(
r#"def compute_{file_id}_{func_id}(a, b, c):
    x = a * {v1} + b * {v2}
    y = c * {v3} - a * {v4}
    for i in range({v5}):
        x = x + i * {v6}
        y = y - i * {v7}
        if x > {v8}:
            x = x % {v9}
    return x + y + {v10}

"#,
        file_id = file_id,
        func_id = func_id,
        v1 = file_id * 17 + func_id * 3 + 1,
        v2 = file_id * 13 + func_id * 7 + 2,
        v3 = file_id * 11 + func_id * 5 + 3,
        v4 = file_id * 7 + func_id * 11 + 4,
        v5 = (file_id + func_id) % 20 + 5,
        v6 = file_id * 3 + func_id + 1,
        v7 = file_id + func_id * 2 + 1,
        v8 = 5000 + file_id * 100 + func_id * 10,
        v9 = 1000 + file_id * 50 + func_id * 5,
        v10 = file_id * func_id + 1
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

"#,
        func_id = func_id
    )
}
