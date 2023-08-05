import hashlib
import multiprocessing
import os


def hash_file_chunk(chunk):
    return hashlib.blake2b(chunk).hexdigest()


def calculate_blake2b_hash(file_path):
    chunk_size = 655366

    with open(file_path, 'rb') as file:
        with multiprocessing.Pool() as pool:
            hash_list = pool.map(hash_file_chunk, iter(lambda: file.read(chunk_size), b''))

    combined_hash = hashlib.blake2b()
    for hash_digest in hash_list:
        combined_hash.update(hash_digest.encode('utf-8'))

    return combined_hash.hexdigest()


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
                all_files[file_path] = calculate_blake2b_hash(file_path)
    return all_files


if __name__ == "__main__":
    path = 'F:\\'
    all_files_with_digests = list_files(path)

    with open(str(path[0]) + ' baselines.txt', 'w') as file:
        for file_path, digest in all_files_with_digests.items():
            file.write(file_path + ': ' + digest + '\n')

    print("File paths with their corresponding BLAKE2b hash digests are stored in 'files_with_digests.txt'.")
