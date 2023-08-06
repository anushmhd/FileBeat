import os
import time
import multiprocessing
import Hashing
import sys
import User_Interface
import colors
import notification


def read_baseline_files(baseline_path):
    data = {}
    with open(baseline_path, 'r') as f:
        for line in f:
            path, hexdigest = line.strip().split("%")
            data[path] = hexdigest
    return data


def integrity_monitoring(file_path, baseline_list):
    while True:
        for baseline_data in baseline_list:
            for path, digest in baseline_data.items():
                if not os.path.exists(path):
                    msg = "ALERT: File at path " + path + " has been deleted or moved"
                    notification.display_notification(msg)
                else:
                    current_hash = Hashing.calculate_hash(path)
                    if current_hash != digest:
                        msg = "ALERT: File at path " + path + " has been modified"
                        notification.display_notification(msg)
        time.sleep(60)


def main():
    User_Interface.clrscr()
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
    main()
