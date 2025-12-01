use std::path::PathBuf;

#[derive(Debug, Clone, PartialEq)]
pub enum ConfigError {
    MinLenExceedsMaxLen { min_len: usize, max_len: usize },
    InvalidEditThreshold(f64),
    InvalidShingleSize(usize),
    MinhashSizeTooSmall { minhash_size: usize, lsh_bands: usize },
}

impl std::fmt::Display for ConfigError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            ConfigError::MinLenExceedsMaxLen { min_len, max_len } => {
                write!(f, "min_len ({}) must be less than max_len ({})", min_len, max_len)
            }
            ConfigError::InvalidEditThreshold(t) => {
                write!(f, "edit_threshold ({}) must be in range [0.0, 1.0]", t)
            }
            ConfigError::InvalidShingleSize(s) => {
                write!(f, "shingle_size ({}) must be > 0", s)
            }
            ConfigError::MinhashSizeTooSmall { minhash_size, lsh_bands } => {
                write!(
                    f,
                    "minhash_size ({}) should be >= lsh_bands ({}) for proper band distribution",
                    minhash_size, lsh_bands
                )
            }
        }
    }
}

impl std::error::Error for ConfigError {}

#[derive(Debug, Clone)]
pub struct Config {
    pub path: PathBuf,
    pub extensions: Vec<String>,
    pub min_len: usize,
    pub max_len: usize,
    pub edit_threshold: f64,
    pub shingle_size: usize,
    pub minhash_size: usize,
    pub lsh_bands: usize,
    pub json_output: bool,
}

impl Default for Config {
    fn default() -> Self {
        Config {
            path: PathBuf::from("."),
            extensions: vec![],
            min_len: 10,
            max_len: 500,
            edit_threshold: 0.15,
            shingle_size: 5,
            minhash_size: 128,
            lsh_bands: 32,
            json_output: false,
        }
    }
}

impl Config {
    pub fn validate(&self) -> Result<(), ConfigError> {
        if self.min_len >= self.max_len {
            return Err(ConfigError::MinLenExceedsMaxLen {
                min_len: self.min_len,
                max_len: self.max_len,
            });
        }

        if !(0.0..=1.0).contains(&self.edit_threshold) {
            return Err(ConfigError::InvalidEditThreshold(self.edit_threshold));
        }

        if self.shingle_size == 0 {
            return Err(ConfigError::InvalidShingleSize(self.shingle_size));
        }

        if self.minhash_size < self.lsh_bands {
            return Err(ConfigError::MinhashSizeTooSmall {
                minhash_size: self.minhash_size,
                lsh_bands: self.lsh_bands,
            });
        }

        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_config_passes() {
        assert!(Config::default().validate().is_ok());
    }

    #[test]
    fn test_min_len_exceeds_max_len() {
        let config = Config {
            min_len: 100,
            max_len: 50,
            ..Config::default()
        };
        assert_eq!(
            config.validate(),
            Err(ConfigError::MinLenExceedsMaxLen { min_len: 100, max_len: 50 })
        );
    }

    #[test]
    fn test_min_len_equals_max_len() {
        let config = Config {
            min_len: 100,
            max_len: 100,
            ..Config::default()
        };
        assert!(config.validate().is_err());
    }

    #[test]
    fn test_edit_threshold_too_high() {
        let config = Config {
            edit_threshold: 1.5,
            ..Config::default()
        };
        assert_eq!(
            config.validate(),
            Err(ConfigError::InvalidEditThreshold(1.5))
        );
    }

    #[test]
    fn test_edit_threshold_negative() {
        let config = Config {
            edit_threshold: -0.1,
            ..Config::default()
        };
        assert!(config.validate().is_err());
    }

    #[test]
    fn test_edit_threshold_boundaries() {
        let config_zero = Config {
            edit_threshold: 0.0,
            ..Config::default()
        };
        assert!(config_zero.validate().is_ok());

        let config_one = Config {
            edit_threshold: 1.0,
            ..Config::default()
        };
        assert!(config_one.validate().is_ok());
    }

    #[test]
    fn test_shingle_size_zero() {
        let config = Config {
            shingle_size: 0,
            ..Config::default()
        };
        assert_eq!(
            config.validate(),
            Err(ConfigError::InvalidShingleSize(0))
        );
    }

    #[test]
    fn test_minhash_size_less_than_bands() {
        let config = Config {
            minhash_size: 16,
            lsh_bands: 32,
            ..Config::default()
        };
        assert_eq!(
            config.validate(),
            Err(ConfigError::MinhashSizeTooSmall {
                minhash_size: 16,
                lsh_bands: 32
            })
        );
    }

    #[test]
    fn test_minhash_size_equals_bands() {
        let config = Config {
            minhash_size: 32,
            lsh_bands: 32,
            ..Config::default()
        };
        assert!(config.validate().is_ok());
    }
}
