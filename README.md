# FileBeat

A Windows based File Integrity Monitor written on python

File System Interaction Module: This module will handle reading and interacting with the file system, including scanning directories, listing files, and reading file contents.

Hashing Module: Implement functions to calculate cryptographic hashes (e.g., MD5, SHA-256, SHA-512) of files. Hashing is essential for verifying file integrity and detecting any unauthorized changes.

Database Module: Create a database or data structure to store file information, including file paths, file hashes, timestamps, etc. This module will be used to maintain a baseline of file integrity.

Baseline Generation Module: Build a module to create a baseline of file integrity. This involves scanning the system, calculating hashes, and storing the results in the database. The baseline will be used as a reference for future integrity checks.

Integrity Verification Module: Develop functions to verify file integrity by comparing the current state of files against the stored baseline in the database. Any discrepancies, such as changed file content or new files, should be identified.

Reporting Module: Design a reporting module to generate detailed reports about file integrity checks. The report should include information about changes, new files, and potential security risks.

Configuration Module: Implement a configuration module to allow users to specify which directories to scan, which hashing algorithms to use, and other customizable options.

Logging Module: Include a logging mechanism to record the results of each integrity check, including any errors or anomalies encountered during the process.