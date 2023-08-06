import hashlib
import multiprocessing


def hash_file_chunk(chunk):
    return hashlib.blake2b(chunk).hexdigest()


def calculate_hash(file_path):
    chunk_size = 655366

    with open(file_path, 'rb') as file:
        with multiprocessing.Pool() as pool:
            hash_list = pool.map(hash_file_chunk, iter(lambda: file.read(chunk_size), b''))

    combined_hash = hashlib.blake2b()
    for hash_digest in hash_list:
        combined_hash.update(hash_digest.encode('utf-8'))

    return combined_hash.hexdigest()


