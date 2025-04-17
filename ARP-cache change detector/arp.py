from scapy.all import *

ARP_TABLE = ({'0.0.0.0': '00:00:00:00:00:00'},
             )

def add_entry(new_entry:dict):
    global ARP_TABLE
    ARP_TABLE = list(ARP_TABLE)
    ARP_TABLE.append(new_entry)
    ARP_TABLE = tuple(ARP_TABLE)
    
pkt = Ether()/ARP()
pkt.dst = "ff:ff:ff:ff:ff:ff"
pkt.pdst = "10.10.10.1"
pkt.show()
new_dict = {pkt.pdst: ''}

answered, unanswered = srp(pkt, timeout=2, verbose=False)

if not answered:
    print("No response recieved.\nPossibly unreachable host or invalid IP")
else:
    for send, recv in answered:
        print("-"*50)
        print("Recieved packet: ")
        recv.show()
        print("-"*50)
    
    new_dict[pkt.pdst] = recv.hwsrc
    add_entry(new_dict)

for entry in ARP_TABLE:
    print(entry)


# 