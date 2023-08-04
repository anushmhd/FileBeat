import ctypes


def fetch_drive_names():

    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()   # detects the disk partitions
    for letter in range(65, 91):
        if bitmask & (1 << (letter - 65)):
            drives.append(chr(letter))
    return ", ".join(drives)