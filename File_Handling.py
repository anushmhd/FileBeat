import ctypes


def fetch_drive_names():

    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()   # detects the disk partitions
    for letter in range(65, 91):
        if bitmask & (1 << (letter - 65)):
            drive_letter = chr(letter)
            if drive_letter != 'C':  # Skipping C drive
                drives.append(drive_letter)
    return drives