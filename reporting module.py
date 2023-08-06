import os
import json

def generate_report(verified_files, baseline_files):
    """
    Generates a detailed report about file integrity checks.

    Args:
        verified_files (dict): Dictionary containing verified file information.
                               Keys are file paths, values are tuples of (hash, timestamp).
        baseline_files (dict): Dictionary containing baseline file information.
                               Keys are file paths, values are tuples of (hash, timestamp).

    Returns:
        str: The report as a formatted string.
    """
    report = []
    report.append("File Integrity Report:")
    report.append("=======================")

    # Identify changes and new files
    changed_files = {}
    new_files = {}
    for path, (hash_value, timestamp) in verified_files.items():
        if path in baseline_files:
            if hash_value != baseline_files[path][0]:
                changed_files[path] = (baseline_files[path][0], hash_value)
        else:
            new_files[path] = (hash_value, timestamp)

    # Generate report content
    if changed_files:
        report.append("\nChanged Files:")
        for path, (old_hash, new_hash) in changed_files.items():
            report.append(f"File: {path}")
            report.append(f"Old Hash: {old_hash}")
            report.append(f"New Hash: {new_hash}")
            report.append("------------------")

    if new_files:
        report.append("\nNew Files:")
        for path, (hash_value, timestamp) in new_files.items():
            report.append(f"File: {path}")
            report.append(f"Hash: {hash_value}")
            report.append(f"Timestamp: {timestamp}")
            report.append("------------------")

    # Generate final report string
    report_str = "\n".join(report)
    return report_str


