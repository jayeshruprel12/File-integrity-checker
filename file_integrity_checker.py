import hashlib
import os
import argparse
import json

HASH_FILE = "file_hashes.json"

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"ERROR: {e}"

def scan_directory(directory):
    """Recursively scan a directory and compute hashes of all files."""
    file_hashes = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hashes[filepath] = calculate_hash(filepath)
    return file_hashes

def create_baseline(directory):
    """Create a baseline of file hashes and save it."""
    print(f"Creating baseline for directory: {directory}")
    hashes = scan_directory(directory)
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)
    print(f"Baseline saved to {HASH_FILE}")

def check_integrity(directory):
    """Compare current file hashes with baseline to detect changes."""
    print(f"Checking file integrity for directory: {directory}")
    if not os.path.exists(HASH_FILE):
        print("No baseline found. Run in 'baseline' mode first.")
        return

    with open(HASH_FILE, "r") as f:
        old_hashes = json.load(f)

    new_hashes = scan_directory(directory)

    modified = []
    added = []
    deleted = []

    # Check for modified and deleted files
    for filepath in old_hashes:
        if filepath not in new_hashes:
            deleted.append(filepath)
        elif old_hashes[filepath] != new_hashes[filepath]:
            modified.append(filepath)

    # Check for new files
    for filepath in new_hashes:
        if filepath not in old_hashes:
            added.append(filepath)

    print("\nIntegrity Check Report:")
    print("========================")
    if modified:
        print("[Modified Files]")
        for f in modified:
            print(f)
    if deleted:
        print("\n[Deleted Files]")
        for f in deleted:
            print(f)
    if added:
        print("\n[New Files Added]")
        for f in added:
            print(f)

    if not (modified or deleted or added):
        print("No changes detected. All files are intact.")

def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker using Hashing")
    parser.add_argument("mode", choices=["baseline", "check"], help="Mode to run the script")
    parser.add_argument("directory", help="Directory to monitor")

    args = parser.parse_args()

    if args.mode == "baseline":
        create_baseline(args.directory)
    elif args.mode == "check":
        check_integrity(args.directory)

if __name__ == "__main__":
    main()
