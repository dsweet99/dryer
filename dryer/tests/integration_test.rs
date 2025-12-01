//! Integration tests validating duplicate detection against tests/fake_code fixtures.
//!
//! These tests verify that the dryer tool correctly identifies the duplicates
//! documented in tests/fake_code/EXPECTED_DUPLICATES.md

use dryer::config::Config;
use dryer::edit_distance::Duplicate;
use std::path::PathBuf;

/// Create a config targeting the fake_code directory
fn test_config() -> Config {
    Config {
        path: PathBuf::from("../tests/fake_code"),
        extensions: vec!["py".to_string()],
        min_len: 10,
        max_len: 500,
        edit_threshold: 0.15,
        shingle_size: 5,
        minhash_size: 128,
        lsh_bands: 32,
        json_output: false,
    }
}

/// Helper to check if a duplicate pair exists (in either order)
fn has_duplicate_between(duplicates: &[Duplicate], file1: &str, file2: &str) -> bool {
    duplicates.iter().any(|d| {
        let f1 = d.chunk1.file.to_string_lossy();
        let f2 = d.chunk2.file.to_string_lossy();
        (f1.contains(file1) && f2.contains(file2)) || (f1.contains(file2) && f2.contains(file1))
    })
}

/// Helper to check if a same-file duplicate exists
fn has_same_file_duplicate(duplicates: &[Duplicate], file: &str) -> bool {
    duplicates.iter().any(|d| {
        let f1 = d.chunk1.file.to_string_lossy();
        let f2 = d.chunk2.file.to_string_lossy();
        f1.contains(file) && f2.contains(file)
    })
}

#[test]
fn test_finds_duplicates_in_fake_code() {
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    // Should find some duplicates
    assert!(
        !duplicates.is_empty(),
        "Should find duplicates in fake_code"
    );
}

#[test]
fn test_cross_file_exact_duplicate_validate_email() {
    // EXPECTED_DUPLICATES.md: utils.py:validate_email == models.py:validate_email (exact copy)
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    assert!(
        has_duplicate_between(&duplicates, "utils.py", "models.py"),
        "Should find duplicate between utils.py and models.py (validate_email)"
    );
}

#[test]
fn test_cross_file_near_duplicate_validate_phone() {
    // EXPECTED_DUPLICATES.md: utils.py:validate_phone vs models.py:validate_phone_number
    // Variable rename phone -> phone_number, ~0.05 distance
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    // This is a near-duplicate, should be caught with 0.15 threshold
    assert!(
        has_duplicate_between(&duplicates, "utils.py", "models.py"),
        "Should find near-duplicate validate_phone functions"
    );
}

#[test]
fn test_cross_file_near_duplicate_calculate_order_total() {
    // EXPECTED_DUPLICATES.md: utils.py:calculate_order_total vs services.py:compute_order_total
    // Renamed params, variable names, ~0.08 distance
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    assert!(
        has_duplicate_between(&duplicates, "utils.py", "services.py"),
        "Should find near-duplicate calculate/compute_order_total"
    );
}

#[test]
fn test_same_file_duplicate_process_user_data() {
    // EXPECTED_DUPLICATES.md: utils.py has process_user_data_v1 and _v2
    // Only diff is .lower() vs .upper()
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    assert!(
        has_same_file_duplicate(&duplicates, "utils.py"),
        "Should find same-file duplicate in utils.py (process_user_data)"
    );
}

#[test]
fn test_same_file_duplicate_config_parsers() {
    // EXPECTED_DUPLICATES.md: models.py has parse_database_config and parse_cache_config
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    assert!(
        has_same_file_duplicate(&duplicates, "models.py"),
        "Should find same-file duplicate in models.py (config parsers)"
    );
}

#[test]
fn test_same_file_duplicate_fetch_functions() {
    // EXPECTED_DUPLICATES.md: services.py has fetch_user_by_id, fetch_product_by_id, fetch_order_by_id
    // These have more variance (entity names, error messages) so need looser threshold
    let config = Config {
        edit_threshold: 0.20, // Looser threshold for these more varied duplicates
        ..test_config()
    };
    let duplicates = dryer::run(config).expect("run should succeed");

    assert!(
        has_same_file_duplicate(&duplicates, "services.py"),
        "Should find same-file duplicates in services.py (fetch functions)"
    );
}

#[test]
fn test_all_duplicates_within_threshold() {
    let config = test_config();
    let threshold = config.edit_threshold;
    let duplicates = dryer::run(config).expect("run should succeed");

    for dup in &duplicates {
        assert!(
            dup.normalized_distance <= threshold,
            "Duplicate should have distance <= {}: got {} between {:?} and {:?}",
            threshold,
            dup.normalized_distance,
            dup.chunk1.file,
            dup.chunk2.file
        );
    }
}

#[test]
fn test_no_overlapping_same_file_duplicates() {
    // Chunks from the same file that overlap should be filtered out
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    for dup in &duplicates {
        if dup.chunk1.file == dup.chunk2.file {
            // Same file - ranges should NOT overlap
            let overlaps = !(dup.chunk1.end_line < dup.chunk2.start_line
                || dup.chunk2.end_line < dup.chunk1.start_line);
            assert!(
                !overlaps,
                "Same-file duplicate should not have overlapping lines: {:?} lines {}-{} vs {}-{}",
                dup.chunk1.file,
                dup.chunk1.start_line,
                dup.chunk1.end_line,
                dup.chunk2.start_line,
                dup.chunk2.end_line
            );
        }
    }
}

#[test]
fn test_scans_subdirectories() {
    // Should find duplicates involving api/handlers.py
    let config = test_config();
    let duplicates = dryer::run(config).expect("run should succeed");

    let has_handlers = duplicates.iter().any(|d| {
        d.chunk1.file.to_string_lossy().contains("handlers.py")
            || d.chunk2.file.to_string_lossy().contains("handlers.py")
    });

    // handlers.py contains build_success_response and build_error_response
    // which should be detected as duplicates
    assert!(
        has_handlers,
        "Should scan subdirectories and find duplicates in api/handlers.py"
    );
}

#[test]
fn test_extension_filtering() {
    // Create config that only looks at .rs files (none exist in fake_code)
    let config = Config {
        path: PathBuf::from("../tests/fake_code"),
        extensions: vec!["rs".to_string()],
        min_len: 10,
        max_len: 500,
        edit_threshold: 0.15,
        shingle_size: 5,
        minhash_size: 128,
        lsh_bands: 32,
        json_output: false,
    };
    let duplicates = dryer::run(config).expect("run should succeed");

    // Should find no duplicates since there are no .rs files
    assert!(
        duplicates.is_empty(),
        "Should find no duplicates when filtering for non-existent extensions"
    );
}

#[test]
fn test_higher_threshold_finds_more() {
    let strict_config = Config {
        edit_threshold: 0.05,
        ..test_config()
    };
    let loose_config = Config {
        edit_threshold: 0.25,
        ..test_config()
    };

    let strict_dups = dryer::run(strict_config).expect("run should succeed");
    let loose_dups = dryer::run(loose_config).expect("run should succeed");

    // Looser threshold should find at least as many duplicates
    assert!(
        loose_dups.len() >= strict_dups.len(),
        "Looser threshold should find >= duplicates: strict={}, loose={}",
        strict_dups.len(),
        loose_dups.len()
    );
}

#[test]
fn test_unique_algorithms_not_matched() {
    // EXPECTED_DUPLICATES.md Control Group: fibonacci and quicksort should NOT match anything
    let config = Config {
        edit_threshold: 0.30, // Even with loose threshold
        ..test_config()
    };
    let duplicates = dryer::run(config).expect("run should succeed");

    // Check that fibonacci and quicksort aren't matching each other
    let fib_quick_match = duplicates.iter().any(|d| {
        let c1 = d.chunk1.original.to_lowercase();
        let c2 = d.chunk2.original.to_lowercase();
        (c1.contains("fibonacci") && c2.contains("quicksort"))
            || (c1.contains("quicksort") && c2.contains("fibonacci"))
    });

    assert!(
        !fib_quick_match,
        "Unique algorithms (fibonacci, quicksort) should not match each other"
    );
}

// =============================================================================
// REGRESSION TESTS FOR FIXED BUGS
// =============================================================================

/// Regression test for Bug #2: Parameter validation
/// Previously, invalid configs would silently produce wrong results.
/// Now run() validates config and returns an error for invalid parameters.
#[test]
fn test_regression_invalid_config_min_exceeds_max() {
    let config = Config {
        min_len: 500,
        max_len: 100, // Invalid: min > max
        ..test_config()
    };

    let result = dryer::run(config);
    assert!(
        result.is_err(),
        "run() should fail when min_len > max_len"
    );
}

#[test]
fn test_regression_invalid_config_edit_threshold_out_of_range() {
    let config = Config {
        edit_threshold: 1.5, // Invalid: > 1.0
        ..test_config()
    };

    let result = dryer::run(config);
    assert!(
        result.is_err(),
        "run() should fail when edit_threshold > 1.0"
    );
}

#[test]
fn test_regression_invalid_config_shingle_size_zero() {
    let config = Config {
        shingle_size: 0, // Invalid: must be > 0
        ..test_config()
    };

    let result = dryer::run(config);
    assert!(
        result.is_err(),
        "run() should fail when shingle_size is 0"
    );
}

#[test]
fn test_regression_invalid_config_minhash_less_than_bands() {
    let config = Config {
        minhash_size: 8,
        lsh_bands: 32, // Invalid: minhash_size < lsh_bands
        ..test_config()
    };

    let result = dryer::run(config);
    assert!(
        result.is_err(),
        "run() should fail when minhash_size < lsh_bands"
    );
}

