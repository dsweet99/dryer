//! Scoring system for ranking duplicate matches.
//!
//! Each match is assigned a feature vector, and a linear combination
//! of normalized features produces the final score.

use serde::{Deserialize, Serialize};
use std::fs;
use std::path::PathBuf;

/// Feature vector for a single match location
#[derive(Debug, Clone)]
pub struct FeatureVector {
    /// Number of members in the cluster this match belongs to
    pub cluster_size: usize,
    /// Mean normalized edit distance to other cluster members
    pub mean_distance: f64,
    /// Number of characters in the match
    pub char_count: usize,
    /// Distance from top of file (in characters) to start of match
    pub file_offset: usize,
    /// Number of lines in the match
    pub line_count: usize,
}

/// Configuration for a single feature
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FeatureConfig {
    /// Weight in [-1, 1]; sum of |weights| across all features should equal 1
    pub weight: f64,
    /// Denominator for normalization: `normalized_value = raw_value / denominator`
    pub denominator: f64,
}

impl Default for FeatureConfig {
    fn default() -> Self {
        Self {
            weight: 0.0,
            denominator: 1.0,
        }
    }
}

/// Scoring configuration for all features
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ScoringConfig {
    pub cluster_size: FeatureConfig,
    pub mean_distance: FeatureConfig,
    pub char_count: FeatureConfig,
    pub file_offset: FeatureConfig,
    pub line_count: FeatureConfig,
}

impl Default for ScoringConfig {
    fn default() -> Self {
        // Default weights: prioritize lower distance, larger clusters, longer matches
        Self {
            cluster_size: FeatureConfig {
                weight: 0.2,
                denominator: 10.0,
            },
            mean_distance: FeatureConfig {
                weight: -0.3, // Negative: lower distance is better
                denominator: 0.15,
            },
            char_count: FeatureConfig {
                weight: 0.2,
                denominator: 500.0,
            },
            file_offset: FeatureConfig {
                weight: -0.1, // Negative: earlier in file is slightly better
                denominator: 10000.0,
            },
            line_count: FeatureConfig {
                weight: 0.2,
                denominator: 20.0,
            },
        }
    }
}

impl ScoringConfig {
    /// Load config from ~/.dryer, creating default if it doesn't exist
    pub fn load() -> Self {
        let config_path = Self::config_path();
        
        if let Some(path) = &config_path {
            if path.exists() {
                if let Ok(contents) = fs::read_to_string(path) {
                    if let Ok(config) = toml::from_str(&contents) {
                        return config;
                    }
                    eprintln!("Warning: Failed to parse ~/.dryer, using defaults");
                }
            } else {
                // Create default config file
                let default = Self::default();
                if let Ok(toml_str) = toml::to_string_pretty(&default) {
                    let contents = format!(
                        "# dryer scoring configuration\n\
                         # Weights should be in [-1, 1] and sum of |weights| should equal 1\n\
                         # score = sum(weight_i * feature_i / denominator_i)\n\n\
                         {toml_str}"
                    );
                    if let Err(e) = fs::write(path, contents) {
                        eprintln!("Warning: Could not create ~/.dryer: {e}");
                    }
                }
                return default;
            }
        }
        
        Self::default()
    }

    /// Get the config file path (~/.dryer)
    fn config_path() -> Option<PathBuf> {
        dirs::home_dir().map(|h| h.join(".dryer"))
    }

    /// Compute score for a feature vector
    /// Each normalized feature is clamped to [0, 1] before weighting
    #[allow(clippy::cast_precision_loss)] // Feature values are small enough that precision loss is negligible
    pub fn score(&self, features: &FeatureVector) -> f64 {
        let clamp = |x: f64| x.clamp(0.0, 1.0);
        
        let mut score = 0.0;
        
        score += self.cluster_size.weight * clamp(features.cluster_size as f64 / self.cluster_size.denominator);
        score += self.mean_distance.weight * clamp(features.mean_distance / self.mean_distance.denominator);
        score += self.char_count.weight * clamp(features.char_count as f64 / self.char_count.denominator);
        score += self.file_offset.weight * clamp(features.file_offset as f64 / self.file_offset.denominator);
        score += self.line_count.weight * clamp(features.line_count as f64 / self.line_count.denominator);
        
        score
    }

    /// Validate that weights sum to 1 (by absolute value)
    pub fn validate(&self) -> Result<(), String> {
        let weights = [
            self.cluster_size.weight,
            self.mean_distance.weight,
            self.char_count.weight,
            self.file_offset.weight,
            self.line_count.weight,
        ];

        // Check each weight is in [-1, 1]
        for (i, &w) in weights.iter().enumerate() {
            if !(-1.0..=1.0).contains(&w) {
                let names = ["cluster_size", "mean_distance", "char_count", "file_offset", "line_count"];
                return Err(format!("{} weight {} is not in [-1, 1]", names[i], w));
            }
        }

        // Check sum of absolute values
        let abs_sum: f64 = weights.iter().map(|w| w.abs()).sum();
        if (abs_sum - 1.0).abs() > 0.001 {
            return Err(format!("Sum of |weights| is {abs_sum}, should be 1.0"));
        }

        // Check denominators are positive
        let denoms = [
            ("cluster_size", self.cluster_size.denominator),
            ("mean_distance", self.mean_distance.denominator),
            ("char_count", self.char_count.denominator),
            ("file_offset", self.file_offset.denominator),
            ("line_count", self.line_count.denominator),
        ];
        for (name, d) in denoms {
            if d <= 0.0 {
                return Err(format!("{name} denominator must be positive, got {d}"));
            }
        }

        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_default_config_is_valid() {
        let config = ScoringConfig::default();
        assert!(config.validate().is_ok());
    }

    #[test]
    fn test_score_computation() {
        let config = ScoringConfig::default();
        let features = FeatureVector {
            cluster_size: 5,
            mean_distance: 0.1,
            char_count: 250,
            file_offset: 1000,
            line_count: 10,
        };
        
        let score = config.score(&features);
        // Just verify it produces a reasonable number
        assert!(score.is_finite());
    }

    #[test]
    fn test_invalid_weight_range() {
        let mut config = ScoringConfig::default();
        config.cluster_size.weight = 1.5;
        assert!(config.validate().is_err());
    }

    #[test]
    fn test_invalid_weight_sum() {
        let config = ScoringConfig {
            cluster_size: FeatureConfig { weight: 0.5, denominator: 10.0 },
            mean_distance: FeatureConfig { weight: 0.5, denominator: 0.15 },
            char_count: FeatureConfig { weight: 0.5, denominator: 500.0 },
            file_offset: FeatureConfig { weight: 0.0, denominator: 10000.0 },
            line_count: FeatureConfig { weight: 0.0, denominator: 20.0 },
        };
        assert!(config.validate().is_err());
    }

    #[test]
    fn test_invalid_denominator() {
        let mut config = ScoringConfig::default();
        config.char_count.denominator = 0.0;
        assert!(config.validate().is_err());
    }

    #[test]
    fn test_score_clamping() {
        // Create a config where we can easily verify clamping
        let config = ScoringConfig {
            cluster_size: FeatureConfig { weight: 1.0, denominator: 10.0 },
            mean_distance: FeatureConfig { weight: 0.0, denominator: 1.0 },
            char_count: FeatureConfig { weight: 0.0, denominator: 1.0 },
            file_offset: FeatureConfig { weight: 0.0, denominator: 1.0 },
            line_count: FeatureConfig { weight: 0.0, denominator: 1.0 },
        };

        // Value above denominator should clamp to 1.0
        let features_high = FeatureVector {
            cluster_size: 100, // 100/10 = 10, clamped to 1.0
            mean_distance: 0.0,
            char_count: 0,
            file_offset: 0,
            line_count: 0,
        };
        assert!((config.score(&features_high) - 1.0).abs() < 0.001);

        // Value at half denominator should be 0.5
        let features_mid = FeatureVector {
            cluster_size: 5, // 5/10 = 0.5
            mean_distance: 0.0,
            char_count: 0,
            file_offset: 0,
            line_count: 0,
        };
        assert!((config.score(&features_mid) - 0.5).abs() < 0.001);
    }

    #[test]
    fn test_negative_weight_lowers_score() {
        // Negative weight means higher feature value = lower score
        let config = ScoringConfig {
            cluster_size: FeatureConfig { weight: 0.0, denominator: 10.0 },
            mean_distance: FeatureConfig { weight: -1.0, denominator: 1.0 },
            char_count: FeatureConfig { weight: 0.0, denominator: 500.0 },
            file_offset: FeatureConfig { weight: 0.0, denominator: 10000.0 },
            line_count: FeatureConfig { weight: 0.0, denominator: 20.0 },
        };

        let low_distance = FeatureVector {
            cluster_size: 2,
            mean_distance: 0.1, // Low distance
            char_count: 100,
            file_offset: 0,
            line_count: 5,
        };
        let high_distance = FeatureVector {
            cluster_size: 2,
            mean_distance: 0.9, // High distance
            char_count: 100,
            file_offset: 0,
            line_count: 5,
        };

        let low_score = config.score(&low_distance);
        let high_score = config.score(&high_distance);
        
        // Lower distance should produce higher (less negative) score
        assert!(low_score > high_score, "low_score {low_score} should be > high_score {high_score}");
    }

    #[test]
    fn test_score_bounds() {
        // With default config, score should be bounded
        let config = ScoringConfig::default();
        
        // Extreme low values
        let min_features = FeatureVector {
            cluster_size: 0,
            mean_distance: 0.0,
            char_count: 0,
            file_offset: 0,
            line_count: 0,
        };
        
        // Extreme high values
        let max_features = FeatureVector {
            cluster_size: 1000,
            mean_distance: 1.0,
            char_count: 10000,
            file_offset: 100_000,
            line_count: 500,
        };
        
        let min_score = config.score(&min_features);
        let max_score = config.score(&max_features);
        
        // Scores should be bounded to [-1, 1] due to clamping and weight constraints
        assert!((-1.0..=1.0).contains(&min_score), "min_score {min_score} out of bounds");
        assert!((-1.0..=1.0).contains(&max_score), "max_score {max_score} out of bounds");
    }

    #[test]
    fn test_toml_serialization_roundtrip() {
        let config = ScoringConfig::default();
        let toml_str = toml::to_string(&config).expect("serialization should work");
        let parsed: ScoringConfig = toml::from_str(&toml_str).expect("deserialization should work");
        
        assert!((config.cluster_size.weight - parsed.cluster_size.weight).abs() < 0.001);
        assert!((config.mean_distance.weight - parsed.mean_distance.weight).abs() < 0.001);
        assert!((config.char_count.denominator - parsed.char_count.denominator).abs() < 0.001);
    }

    #[test]
    fn test_toml_parsing_custom_config() {
        let toml_str = r"
            [cluster_size]
            weight = 0.5
            denominator = 5.0

            [mean_distance]
            weight = -0.5
            denominator = 0.2

            [char_count]
            weight = 0.0
            denominator = 100.0

            [file_offset]
            weight = 0.0
            denominator = 1000.0

            [line_count]
            weight = 0.0
            denominator = 10.0
        ";
        
        let config: ScoringConfig = toml::from_str(toml_str).expect("parsing should work");
        assert!((config.cluster_size.weight - 0.5).abs() < 0.001);
        assert!((config.mean_distance.weight - (-0.5)).abs() < 0.001);
        assert!((config.cluster_size.denominator - 5.0).abs() < 0.001);
        assert!(config.validate().is_ok());
    }

    #[test]
    fn test_validate_negative_denominator() {
        let mut config = ScoringConfig::default();
        config.file_offset.denominator = -100.0;
        let result = config.validate();
        assert!(result.is_err());
        assert!(result.unwrap_err().contains("file_offset"));
    }

    #[test]
    fn test_validate_weight_below_minus_one() {
        let mut config = ScoringConfig::default();
        config.mean_distance.weight = -1.5;
        let result = config.validate();
        assert!(result.is_err());
        assert!(result.unwrap_err().contains("mean_distance"));
    }

    #[test]
    fn test_all_features_contribute_to_score() {
        // Each feature should independently affect the score
        let base = FeatureVector {
            cluster_size: 5,
            mean_distance: 0.075,
            char_count: 250,
            file_offset: 5000,
            line_count: 10,
        };
        
        let config = ScoringConfig::default();
        let base_score = config.score(&base);
        
        // Increase cluster_size (positive weight) -> higher score
        let bigger_cluster = FeatureVector { cluster_size: 10, ..base };
        assert!(config.score(&bigger_cluster) > base_score);
        
        // Increase mean_distance (negative weight) -> lower score
        let higher_distance = FeatureVector { mean_distance: 0.14, ..base };
        assert!(config.score(&higher_distance) < base_score);
        
        // Increase char_count (positive weight) -> higher score
        let more_chars = FeatureVector { char_count: 400, ..base };
        assert!(config.score(&more_chars) > base_score);
        
        // Increase file_offset (negative weight) -> lower score
        let later_in_file = FeatureVector { file_offset: 9000, ..base };
        assert!(config.score(&later_in_file) < base_score);
        
        // Increase line_count (positive weight) -> higher score
        let more_lines = FeatureVector { line_count: 18, ..base };
        assert!(config.score(&more_lines) > base_score);
    }
}

