import hashlib

import colors


def calculate_hash(file_path, algorithm):

    if algorithm == "1" and "sha1":
        hash_object = hashlib.sha1()
    elif algorithm == "2" and "sha2":
        hash_object = hashlib.sha256()
    elif algorithm == "3" and "sha3":
        hash_object = hashlib.sha3_256()
    else:
        return

    with open(file_path, "rb") as file:
        file_content = file.read()
        hash_object.update(file_content)

    return hash_object.hexdigest()

def baseline(file_path, hash_value):
    with open(file_path, "a") as hash_file:
        hash_file.write(hash_value + "\n")

def main():

    hashing_algorithm = None
    file_path = input("Enter the path to the file: ")
    while True:
        print ("Hashing Algorithms")
        print ("\t1. SHA1 \n\t2. SHA2 \n\t3. SHA3")
        hashing_algorithm = input("Choose from the above: ").lower()
        print(hashing_algorithm)

        if hashing_algorithm == "1" and "sha1":
            hash_value = calculate_hash(file_path, "1")
            print("1")
            break
        elif hashing_algorithm == "2" and "sha2":
            hash_value = calculate_hash(file_path, "2")
            print("2")
            break
        elif hashing_algorithm == "3" and "sha3":
            hash_value = calculate_hash(file_path, "3")
            print("3")
            break
        else:
            colors.print_red("\nInvalid hashing algorithm selected. Please try again!\n")

    if hash_value:
        print(f"Hash ({hashing_algorithm}): {hash_value}")
        baseline("Hashes.txt", hash_value)
        print("Hash saved to Hashes.txt")


if __name__ == "__main__":
    main()
