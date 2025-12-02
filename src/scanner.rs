use ignore::WalkBuilder;
use rayon::prelude::*;
use std::fs;
use std::io;
use std::path::{Path, PathBuf};
use std::sync::Arc;

#[derive(Debug, Clone)]
pub struct SourceFile {
    pub path: Arc<PathBuf>,
    pub content: String,
}

pub fn scan_files(root: &Path, extensions: &[String]) -> io::Result<Vec<SourceFile>> {
    let paths: Vec<PathBuf> = WalkBuilder::new(root)
        .hidden(true)
        .git_ignore(true)
        .git_global(true)
        .git_exclude(true)
        .ignore(true)
        .build()
        .filter_map(Result::ok)
        .filter(|e| e.path().is_file())
        .filter(|e| matches_extension_filter(e.path(), extensions))
        .map(ignore::DirEntry::into_path)
        .collect();

    let files: Vec<SourceFile> = paths
        .into_par_iter()
        .filter_map(|path| try_read_utf8_file(&path))
        .collect();

    Ok(files)
}

fn matches_extension_filter(path: &Path, extensions: &[String]) -> bool {
    if extensions.is_empty() {
        return true;
    }

    let ext = path
        .extension()
        .and_then(|e| e.to_str())
        .unwrap_or("");

    extensions.iter().any(|e| e == ext)
}

fn try_read_utf8_file(path: &Path) -> Option<SourceFile> {
    fs::read_to_string(path).ok().map(|content| SourceFile {
        path: Arc::new(path.to_path_buf()),
        content,
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs::{self, File};
    use std::io::Write;
    use tempfile::TempDir;

    fn create_temp_dir() -> TempDir {
        tempfile::tempdir().unwrap()
    }

    #[test]
    fn test_scan_empty_directory() {
        let dir = create_temp_dir();
        let files = scan_files(dir.path(), &[]).unwrap();
        assert!(files.is_empty());
    }

    #[test]
    fn test_scan_single_file() {
        let dir = create_temp_dir();
        let file_path = dir.path().join("test.py");
        fs::write(&file_path, "def foo(): pass").unwrap();

        let files = scan_files(dir.path(), &[]).unwrap();
        assert_eq!(files.len(), 1);
        assert_eq!(files[0].content, "def foo(): pass");
    }

    #[test]
    fn test_extension_filter_includes_matching() {
        let dir = create_temp_dir();
        fs::write(dir.path().join("test.py"), "python code").unwrap();
        fs::write(dir.path().join("test.rs"), "rust code").unwrap();
        fs::write(dir.path().join("test.js"), "js code").unwrap();

        let extensions = vec!["py".to_string(), "rs".to_string()];
        let files = scan_files(dir.path(), &extensions).unwrap();

        assert_eq!(files.len(), 2);
        let contents: Vec<&str> = files.iter().map(|f| f.content.as_str()).collect();
        assert!(contents.contains(&"python code"));
        assert!(contents.contains(&"rust code"));
        assert!(!contents.contains(&"js code"));
    }

    #[test]
    fn test_extension_filter_empty_means_all() {
        let dir = create_temp_dir();
        fs::write(dir.path().join("test.py"), "python").unwrap();
        fs::write(dir.path().join("test.rs"), "rust").unwrap();
        fs::write(dir.path().join("test.txt"), "text").unwrap();

        let files = scan_files(dir.path(), &[]).unwrap();
        assert_eq!(files.len(), 3);
    }

    #[test]
    fn test_skips_binary_files() {
        let dir = create_temp_dir();

        fs::write(dir.path().join("valid.txt"), "hello world").unwrap();

        let binary_path = dir.path().join("binary.bin");
        let mut f = File::create(&binary_path).unwrap();
        f.write_all(&[0x80, 0x81, 0x82, 0xFF, 0xFE]).unwrap();

        let files = scan_files(dir.path(), &[]).unwrap();

        assert_eq!(files.len(), 1);
        assert_eq!(files[0].content, "hello world");
    }

    #[test]
    fn test_scans_subdirectories() {
        let dir = create_temp_dir();
        let subdir = dir.path().join("subdir");
        fs::create_dir(&subdir).unwrap();

        fs::write(dir.path().join("root.py"), "root file").unwrap();
        fs::write(subdir.join("nested.py"), "nested file").unwrap();

        let files = scan_files(dir.path(), &[]).unwrap();
        assert_eq!(files.len(), 2);
    }

    #[test]
    fn test_file_without_extension() {
        let dir = create_temp_dir();
        fs::write(dir.path().join("Makefile"), "all: build").unwrap();
        fs::write(dir.path().join("test.py"), "python").unwrap();

        let files = scan_files(dir.path(), &[]).unwrap();
        assert_eq!(files.len(), 2);

        let extensions = vec!["py".to_string()];
        let files = scan_files(dir.path(), &extensions).unwrap();
        assert_eq!(files.len(), 1);
    }

    #[test]
    fn test_respects_ignore_file() {
        let dir = create_temp_dir();
        
        fs::write(dir.path().join(".ignore"), "ignored.txt\nbuild/").unwrap();
        fs::write(dir.path().join("included.txt"), "included").unwrap();
        fs::write(dir.path().join("ignored.txt"), "ignored").unwrap();
        let build_dir = dir.path().join("build");
        fs::create_dir(&build_dir).unwrap();
        fs::write(build_dir.join("output.txt"), "build output").unwrap();

        let files = scan_files(dir.path(), &[]).unwrap();
        
        assert_eq!(files.len(), 1);
        assert!(files[0].path.to_string_lossy().contains("included.txt"));
    }
}
