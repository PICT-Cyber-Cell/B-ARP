from pyroute2 import IPRoute
from datetime import datetime
import time

def monitor_ip_assignment():
    ipr = IPRoute()
    ipr.bind()

    print("Monitoring for IP address assignments (press Ctrl+C to stop)...")

    try:
        while True:
            msgs = ipr.get()
            for msg in msgs:
                if msg['header']['type'] == 20:  # RTM_NEWADDR
                    attrs = dict(msg.get('attrs', []))
                    index = msg.get('index')
                    ifa_address = attrs.get('IFA_ADDRESS')
                    ifname = ipr.get_links(index)[0].get_attr('IFLA_IFNAME')
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(f"[{timestamp}] [+] IP address {ifa_address} assigned to interface {ifname}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    finally:
        ipr.close()

if __name__ == "__main__":
    monitor_ip_assignment()
