from scapy.all import Ether, ARP, srp, sniff

BROADCAST = 'FF:FF:FF:FF:FF:FF'

def get_mac(ip):
    """
    Renvoie l'adresse MAC associée à l'adresse IP.
    """

    p = Ether(dst=BROADCAST)/ARP(pdst=IP) # On construit un paquet ARP qu'on broadcast pour demander qui a cette IP?
    ans = srp(p, timeout=3, verbose=False)[0] # envoie & reçoit le paquet p et on récupère les réponses à p

    return ans[0][1].hwsrc # on retourne l'adresse MAC.

def process(packet):
    """
    Callback pour traiter les paquets.
    """

    # Est-ce un paquet ARP?
    if packet.haslayer(ARP):
        if packet[ARP].op == 2: # est-ce une réponse ARP? (et non pas une requête ARP)
            try:
                # Choppons la vraie adresse MAC de l'envoyeur
                real_mac = get_mac(packet[ARP].psrc)
                response_mac = packet[ARP].hwsrc # Avons-nous une fausse déclaration dans le paquet?

                if real_mac != response_mac:
                    print(f"[!] Attaque ARP détectée, adresse MAC réelle: {real_mac}, spoofé: {response_mac}")
            except IndexError:
                # Échec temporaire d'avoir trouvé l'adresse MAC réelle.
                # On l'ignore.
                pass

# Allez, on sniff tout.
sniff(store=False, prn=process)
