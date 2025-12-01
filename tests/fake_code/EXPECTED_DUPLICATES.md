# Expected Duplicates in fake_code

This document catalogs the intentional duplicates for test validation.

## Cross-File Exact Duplicates

| Location A | Location B | Description |
|------------|------------|-------------|
| `utils.py:validate_email` | `models.py:validate_email` | Exact copy |

## Cross-File Near-Duplicates (Low Edit Distance)

| Location A | Location B | Changes | Est. Norm. Distance |
|------------|------------|---------|---------------------|
| `utils.py:validate_phone` | `models.py:validate_phone_number` | Variable rename `phone` → `phone_number` | ~0.05 |
| `utils.py:calculate_order_total` | `services.py:compute_order_total` | Renamed params, variable names | ~0.08 |
| `utils.py:validate_email` | `api/handlers.py:check_valid_email` | Different docstring | ~0.10 |

## Same-File Duplicates

| File | Function A | Function B | Changes |
|------|------------|------------|---------|
| `utils.py` | `process_user_data_v1` | `process_user_data_v2` | `.lower()` → `.upper()` |
| `models.py` | `parse_database_config` | `parse_cache_config` | Connection string prefix, default port |
| `models.py` | `User.to_dict` | `Product.to_dict` | Field names |
| `models.py` | `User.validate` | `Product.validate` | Error messages, price check |
| `services.py` | `fetch_user_by_id` | `fetch_product_by_id` | Entity names |
| `services.py` | `fetch_user_by_id` | `fetch_order_by_id` | Entity names |
| `services.py` | `summarize_sales` | `summarize_expenses` | Variable names |
| `api/handlers.py` | `build_success_response` | `build_error_response` | Status and fields |
| `edge_cases.py` | `log_event_info` | `log_event_warning` | Log level prefix |
| `edge_cases.py` | `log_event_warning` | `log_event_error` | Log level prefix |
| `edge_cases.py` | `outer_process_a` | `outer_process_b` | Pre-processing line |

## Triple+ Duplicates (Same Pattern 3+ Times)

| Pattern | Locations |
|---------|-----------|
| Fetch entity by ID | `services.py`: user, product, order |
| Log event | `edge_cases.py`: info, warning, error |
| Response builders | `api/handlers.py`: success, error, warning |

## Whitespace Variation Tests

| File | Functions | Notes |
|------|-----------|-------|
| `edge_cases.py` | `spaced_out_function`, `compact_function` | Should match after whitespace normalization |

## Short Duplicates (May Be Below Threshold)

| File | Functions | Length |
|------|-----------|--------|
| `edge_cases.py` | `add`, `sub`, `mul`, `div` | ~20 chars each |

## Structural Similarity (Different Content)

| File | Items | Notes |
|------|-------|-------|
| `edge_cases.py` | `greet_user_*` | Same structure, different languages |
| `models.py` | `User`, `Product` dataclasses | Similar fields/methods |

## Control Group (Should NOT Match)

| File | Item | Notes |
|------|------|-------|
| `models.py` | `fibonacci`, `quicksort` | Unique algorithms |
| `edge_cases.py` | `BinarySearchTree` | Unique implementation |

