# FileBeat

A Windows based File Integrity Monitor written on python, that will check for File deletion and Modification. It also notifies the user and stores the log in a PDF report.

The Application uses blake2b hashing algorthim for integrity checking and hashing. 

The Application recursively traverse through all folders in the drive, till 2 depts, Because going into filepath more than 2 depths make the application very slow as it is written on python.It automatically detects the system drives and leaves C Drive intentionally as its very much volatile with lot of cache and log files. 

Usage: 
pip install -r requirements.txt 

python3 main.py

The Application has the following modules:

File System Interaction Module: This module will handle reading and interacting with the file system, including scanning directories, listing files, and reading file contents.

Hashing Module: Implement functions to calculate cryptographic hashes using blake2b algorithm of files. Hashing is essential for verifying file integrity and detecting any unauthorized changes. 

Baseline Generation Module: Build a module to create a baseline of file integrity. This involves scanning the system, calculating hashes, and storing the results in the database. The baseline will be used as a reference for future integrity checks.

Integrity Verification Module: Develop functions to verify file integrity by comparing the current state of files against the stored baseline in the database. Any discrepancies, such as changed file content or deleted/moved files, should be identified.

Reporting Module: Design a reporting module to generate detailed reports about file integrity checks. The report should include information about changes, along with the time stamp

User Interface Module: Implement a configuration module to allow users to specify which directories to scan, which hashing algorithms to use, and other customizable options. This is the main  module

