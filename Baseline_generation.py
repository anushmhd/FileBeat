import os
import Hashing
import sys


def list_files(path):
    all_files = {}
    max_depth = 2
    for root, directories, files in os.walk(path):
        depth = root[len(path) - len(os.path.dirname(path)):].count(os.path.sep)

        directories[:] = [d for d in directories if not d.startswith('.')]

        if depth >= max_depth:
            continue

        for f in files:
            if not f.startswith('.'):
                file_path = os.path.join(root, f)
                all_files[file_path] = Hashing.calculate_hash(file_path)
    return all_files


def main():
    print("Baseline files doesn't exist...\nGenerating New baselines...")
    path = sys.argv
    path.pop(0)

    for i in range(len(path)):
        fpath = path[i]+ ':\\'
        all_files_with_digests = list_files(fpath)

        with open("Baseline\\" + str(fpath[0]) + ' baselines.txt', 'w') as file:
            for file_path, digest in all_files_with_digests.items():
                file.write(file_path + ': ' + digest + '\n')

    print("New Baselines Generated")


if __name__ == "__main__":
    main()
