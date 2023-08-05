import File_Handling
import colors
import os
import time


def display_banner() -> None:
    """
    :rtype: None
    """
    banner = (r"" "\n"
              r" ___         ___  __   ___      ___ " "\n"
              r"|__  | |    |__  |__) |__   /\   |  " "\n"
              r"|    | |___ |___ |__) |___ /~~\  |  " "\n"
              r"                                    " "\n"
              r"    ")
    print(banner)


def animate_progress(text, total_frames=30, interval=0.1):
    for frame in range(total_frames):
        progress = "#" * frame + "-" * (total_frames - frame)
        print(f"\r{text} [{progress}] {frame + 1}/{total_frames}", end="", flush=True)
        time.sleep(interval)


def clrscr():
    os.system("cls")


def get_drives_input(drives):
    while True:
        drives_input = input(f"\nEnter 'all' drives or one or more available drives ({', '.join(drives)}), "
                             f" all separated by"
                             f" commas: ")
        drives_input = drives_input.split(',')

        if not drives_input:
            colors.print_red("Invalid input, Please try again...")
            continue

        if drives_input[0].upper().strip() == "ALL":
            return drives

        drives_input = list(set(drives_input))
        selected_drives = []

        for i in range(len(drives_input)):
            if drives_input[i].upper() not in drives:
                colors.print_red("Invalid input, Please try again...")
                selected_drives = []
                break
            elif drives_input[i].upper() in drives:
                print(drives_input[i])
                selected_drives.append(drives_input[i].upper())

        if len(selected_drives) == 0:
            continue
        else:
            return selected_drives


display_banner()
colors.print_green("Which drives do you want to monitor???")

windows_drives = File_Handling.fetch_drive_names()
print("Available Windows drive partitions:", ", ".join(windows_drives))
input_drives = get_drives_input(windows_drives)
print("You have selected the drives", ", ".join(input_drives))

clrscr()
#animate_progress("Doing Basic checks...")
pc_check = File_Handling.basic_check()

if pc_check:
    File_Handling.check_baseline(input_drives)
else:
    File_Handling.generate_baseline()