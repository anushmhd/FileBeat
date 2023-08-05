import File_Handling
import Colors


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


def get_drives_input(drives):

    while True:
        drives_input = input(f"\nEnter 'all' drives or one or more available drives ({', '.join(drives)}), "
                             f" all separated by"
                             f"commas: ")
        drives_input = drives_input.split(',')

        if not drives_input:
            Colors.print_red("Invalid input, Please try again...")
            continue

        if drives_input[0].upper().strip() == "ALL":
            return drives

        drives_input = list(set(drives_input))
        selected_drives = []

        for i in range(len(drives_input)):
            if drives_input[i].upper() not in drives:
                Colors.print_red("Invalid input, Please try again...")
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
Colors.print_green("Which drives do you want to monitor???")

windows_drives = File_Handling.fetch_drive_names()
print("Available Windows drive partitions:", ", ".join(windows_drives))
input_drives = get_drives_input(windows_drives)
print(input_drives)