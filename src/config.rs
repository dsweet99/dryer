use std::path::PathBuf;

#[derive(Debug, Clone, PartialEq)]
pub enum ConfigError {
    InvalidChunkLines(usize),
    InvalidEditThreshold(f64),
    InvalidShingleSize(usize),
    MinhashSizeTooSmall { minhash_size: usize, lsh_bands: usize },
}

impl std::fmt::Display for ConfigError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::InvalidChunkLines(n) => {
                write!(f, "chunk_lines ({n}) must be >= 3")
            }
            Self::InvalidEditThreshold(t) => {
                write!(f, "edit_threshold ({t}) must be in range [0.0, 1.0]")
            }
            Self::InvalidShingleSize(s) => {
                write!(f, "shingle_size ({s}) must be > 0")
            }
            Self::MinhashSizeTooSmall { minhash_size, lsh_bands } => {
                write!(
                    f,
                    "minhash_size ({minhash_size}) should be >= lsh_bands ({lsh_bands}) for proper band distribution"
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
    pub min_chars: usize,
    pub chunk_lines: usize,
    pub edit_threshold: f64,
    pub shingle_size: usize,
    pub minhash_size: usize,
    pub lsh_bands: usize,
    /// Optional filter: only report duplicates involving these files
    pub filter_files: Vec<PathBuf>,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            path: PathBuf::from("."),
            extensions: vec![],
            min_chars: 50,
            chunk_lines: 10,
            edit_threshold: 0.15,
            shingle_size: 5,
            minhash_size: 128,
            lsh_bands: 32,
            filter_files: vec![],
        }
    }
}

impl Config {
    pub fn validate(&self) -> Result<(), ConfigError> {
        if self.chunk_lines < 3 {
            return Err(ConfigError::InvalidChunkLines(self.chunk_lines));
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
    fn test_chunk_lines_too_small() {
        let config = Config {
            chunk_lines: 2,
            ..Config::default()
        };
        assert_eq!(
            config.validate(),
            Err(ConfigError::InvalidChunkLines(2))
        );
    }

    #[test]
    fn test_chunk_lines_minimum() {
        let config = Config {
            chunk_lines: 3,
            ..Config::default()
        };
        assert!(config.validate().is_ok());
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
