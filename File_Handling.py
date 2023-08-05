import ctypes
import uuid
import os


def fetch_drive_names():
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()  # detects the disk partitions
    for letter in range(65, 91):
        if bitmask & (1 << (letter - 65)):
            drive_letter = chr(letter)
            if drive_letter != 'C':  # Skipping C drive
                drives.append(drive_letter)
    return drives


def check_first_time():
    uid_value = uuid.getnode()
    with open('Baseline/uuid.txt', 'r') as file:
        old_id = file.read()
        file.close()

    if old_id == str(uid_value):
        return True
    else:
        print("New PC")
        with open('Baseline/uuid.txt', 'w') as f:
            f.write(str(uid_value))
            f.close()
        files = os.listdir('Baseline/')

        for f in files:
            print(f)
            if f != 'uuid.txt':
                os.remove("Baseline/" + f)
        return False


check_first_time()

