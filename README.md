# 🛡️ File Integrity Checker (Python)

A Python-based tool to monitor changes in files by calculating and comparing **SHA-256 hash values**. It helps ensure **file integrity** by detecting unauthorized changes, deletions, or additions to files in a given directory.

---

## 🚀 Features

- ✅ Create a secure baseline of file hashes
- 🔍 Check and detect:
  - Modified files
  - Deleted files
  - Newly added files
- 🧰 Uses only standard Python libraries (`hashlib`, `os`, `json`, `argparse`)
- 🗂️ Works recursively on all files in a directory

---

## 📦 Requirements

- Python 3.x installed on your system
- No external libraries needed

---

## 🛠️ How to Use

### 1. **Create a baseline** of current files:
```bash
python file_integrity_checker.py baseline <directory_path>
