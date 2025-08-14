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

### 1️⃣ Create a Baseline

Generate a reference hash of all files in a directory:

```bash
python file_integrity_checker.py baseline <directory_path>
```

### 2️⃣ Check for Changes

Compare current files to the saved baseline:

```bash
python file_integrity_checker.py check <directory_path>
```

---

## 📂 Example Usage

```bash
python file_integrity_checker.py baseline "C:\Users\vikas\Desktop"
python file_integrity_checker.py check "C:\Users\vikas\Desktop"
```

---

## 📁 Output

Generates a `file_hashes.json` file storing SHA-256 hashes.  
Use this file for future comparisons during integrity checks.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

- Author: Jayesh Dilip Ruprel  
- Contact: jayeshruprel16@gmail.com  
🏫 University: DY Patil International University
