import subprocess
import re
import csv
import time
import threading
import os

ARP_FILE = 'arp_cache.csv'
CHECK_INTERVAL = 10  # seconds

def get_arp_table():
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    arp_entries = {}

    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+([a-f0-9\-:]{17})', re.IGNORECASE)
    for line in result.stdout.splitlines():
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            mac = match.group(2).lower()
            arp_entries[ip] = mac

    return arp_entries

def write_to_csv(arp_dict, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Address', 'MAC Address'])
        for ip, mac in arp_dict.items():
            writer.writerow([ip, mac])

def read_from_csv(filename):
    arp_dict = {}
    if not os.path.exists(filename):
        return arp_dict
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arp_dict[row['IP Address']] = row['MAC Address'].lower()
    return arp_dict

def monitor_arp_changes():
    print("Daemon started. Monitoring ARP changes...")
    initial_arp = read_from_csv(ARP_FILE)

    while True:
        current_arp = get_arp_table()
        added = {ip: mac for ip, mac in current_arp.items() if ip not in initial_arp}
        removed = {ip: mac for ip, mac in initial_arp.items() if ip not in current_arp}
        changed = {ip: mac for ip, mac in current_arp.items()
                   if ip in initial_arp and initial_arp[ip] != mac}

        if added or removed or changed:
            print("\n ARP Cache Change Detected!")
            if added:
                print(" Added:")
                for ip, mac in added.items():
                    print(f"  {ip} -> {mac}")
            if removed:
                print(" Removed:")
                for ip, mac in removed.items():
                    print(f"  {ip} -> {mac}")
            if changed:
                print(" Changed:")
                for ip, mac in changed.items():
                    print(f"  {ip}: {initial_arp[ip]} ➜ {mac}")
        else:
            print(" No change detected.")

        time.sleep(CHECK_INTERVAL)

def main():
    # Check if ARP_FILE exists. If not, create it as the initial snapshot.
    if not os.path.exists(ARP_FILE):
        print("Creating initial ARP table snapshot...")
        initial_table = get_arp_table()
        write_to_csv(initial_table, ARP_FILE)
        print(f"Initial ARP cache stored in {ARP_FILE}")

    # Start the monitoring daemon
    daemon_thread = threading.Thread(target=monitor_arp_changes, daemon=True)
    daemon_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping daemon...")

if __name__ == "__main__":
    main()
