import os
import time
import multiprocessing
import Hashing
import sys
import signal
import Report
import File_Handling
import colors
import notification


def handle_keyboard_interrupt(signal_number, frame):
    colors.print_yellow("\nKeyboard interrupt detected. Stopping monitoring processes...\nBye!")
    sys.exit(0)


def read_baseline_files(baseline_path):
    data = {}
    with open(baseline_path, 'r') as f:
        for line in f:
            path, hexdigest = line.strip().split("%")
            data[path] = hexdigest
    return data


def integrity_monitoring(file_path, baseline_list):
    changes = []
    while True:
        for baseline_data in baseline_list:
            for path, digest in baseline_data.items():
                if not os.path.exists(path):
                    msg = "ALERT: File at path " + path + " has been deleted or moved"
                    notification.display_notification(msg)
                    new_change = {"file": os.path.basename(path), "path": path, "change": "Deleted or Moved"}
                    if new_change not in changes:
                        changes.append(new_change)
                else:
                    current_hash = Hashing.calculate_hash(path)
                    if current_hash != digest:
                        msg = "ALERT: File at path " + path + " has been modified"
                        notification.display_notification(msg)
                        new_change = {"file": os.path.basename(path), "path": path, "change": "Modified"}
                        if new_change not in changes:
                            changes.append(new_change)
            Report.gen_report(changes, "FileBeat_Report.pdf")
            time.sleep(60)


def main():
    File_Handling.clrscr()
    colors.print_red("Beginning monitoring of the drives\n")
    path = sys.argv
    path.pop(0)

    baseline_paths = list(map(lambda x: "Baseline\\" + x + " baselines.txt", path))

    baseline_list = [read_baseline_files(baselines) for baselines in baseline_paths]

    pools = []
    for i, filepath in enumerate(path):
        pool = multiprocessing.Process(target=integrity_monitoring, args=(filepath, baseline_list))
        pools.append(pool)
        pool.start()

    for pool in pools:
        pool.join()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_keyboard_interrupt)
    main()
