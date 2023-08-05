import ctypes
import uuid
import os
import datetime

def fetch_drive_names():
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()  # detects the disk partitions
    for letter in range(65, 91):
        if bitmask & (1 << (letter - 65)):
            drive_letter = chr(letter)
            if drive_letter != 'C':  # Skipping C drive
                drives.append(drive_letter)
    return drives


def basic_check() -> bool:
    uid_value = uuid.getnode()
    with open('Baseline/uuid.txt', 'r') as file:
        old_id = file.read()
        file.close()

    if old_id == str(uid_value):
        return True
    else:
        with open('Baseline/uuid.txt', 'w') as f:
            f.write(str(uid_value))
            f.close()
        files = os.listdir('Baseline/')

        for f in files:
            if f != 'uuid.txt':
                os.remove("Baseline/" + f)
        return False


def is_file_non_empty(filepath):
    print(filepath)
    last_mod_stamp = ''
    if os.path.exists(filepath):
        print("file exists")
        if os.path.getsize(filepath) > 0:
            last_mod_time = os.path.getmtime(filepath)
            last_mod_stamp = datetime.datetime.fromtimestamp(last_mod_time)
            return last_mod_stamp, True
        else:
            print("File is empty")
            return last_mod_stamp, False
    else:
        print("File  doesn't exist")
        return last_mod_stamp, False


def check_baseline(chosen_drives):
    print("\n")
    check = True
    for i in range(len(chosen_drives)):
        time_val, val = is_file_non_empty("Baseline/" + str(chosen_drives[i]) + ".txt")
        check = check and val
        print(val)

    if check is True:
        print("\nBaseline exists for the time stamp", time_val)
    else:
        print("\nBaseline doesn't exist")
