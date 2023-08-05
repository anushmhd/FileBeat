import datetime

class ReportingModule:
    def __init__(self, database):
        self.database = database

    def generate_report(self, baseline, current_state):
        report = "File Integrity Report\n"
        report += "Date: {}\n\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Compare the baseline with the current state
        changes, new_files = self.compare_files(baseline, current_state)

        # Reporting changes
        if changes:
            report += "Changes Detected:\n"
            for file_path in changes:
                report += "- File: {}\n".format(file_path)
        else:
            report += "No changes detected.\n"

        # Reporting new files
        if new_files:
            report += "\nNew Files Detected:\n"
            for file_path in new_files:
                report += "- File: {}\n".format(file_path)
        else:
            report += "No new files detected.\n"

        return report

    def compare_files(self, baseline, current_state):
        baseline_files = set(baseline.keys())
        current_files = set(current_state.keys())

        # Find files that have been changed
        changed_files = []
        for file_path in baseline_files.intersection(current_files):
            if baseline[file_path] != current_state[file_path]:
                changed_files.append(file_path)

        # Find new files
        new_files = current_files - baseline_files

        return changed_files, new_files

# Example usage:
if __name__ == "__main__":
    # Assuming you have a database instance named 'database' containing baseline and current_state data
    reporting_module = ReportingModule(database)

    # Assuming you have the baseline and current_state as dictionaries of file paths and their corresponding hashes
    baseline = {
        "/path/to/file1.txt": "hash_of_file1",
        "/path/to/file2.txt": "hash_of_file2",
        # ...
    }

    current_state = {
        "/path/to/file1.txt": "new_hash_of_file1",
        "/path/to/file2.txt": "hash_of_file2",
        "/path/to/new_file.txt": "hash_of_new_file",
        # ...
    }

    report = reporting_module.generate_report(baseline, current_state)
    print(report)
