---
title: QCM de sécurité
author: \textsc{Ryan Lahfa}
advanced-maths: true
advanced-cs: true
---

Indiquez le numéro de chaque réponse que vous estimez être vrai, il peut avoir plusieurs réponses à la même question.

\Question{1} Que retourne `[x**2 for x in range(10)]` en Python?

(1) `[0, 1, 4, 9, 16, 25, 37, 49, 64, 81]`
(2) `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`
(3) `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`

\Question{2} Si on envoie le paquet `Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(op=2, pdst='192.168.1.3', psrc='', hwsrc='00:DE:AD:BE:EF:00')`, quel résultat attend-t-on du cache ARP des personnes qui le recevront, dans l'hypothèse que le routeur/switch n'ait pas de protection contre l'ARP spoofing?

(1) Toutes les personnes qui auront reçu ce paquet diront que l'adresse IP `XXXXXX` est associé à l'adresse MAC `00:DE:AD:BE:EF:00`.
(2) La personne avec l'adresse IP `192.168.1.3` mettra dans son cache ARP que l'adresse IP `XXX` est associé à l'adresse MAC …
(3) Le routeur arrive quand même à empêcher l'attaque

\Question{3} Si on utilise Heartbleed pour tirer de la RAM d'un serveur, quel ordre de grandeur de temps faut-il en général pour obtenir toute la RAM physique de la cible à raison de 100 paquets par seconde ?

(1) 1 mois
(2) 3 jours
(3) 10 heures

\Question{4} Si on essaye de man-in-the-middle google.com ; que faut-il gérer en priorité par exemple pour que les navigateurs web ne nous jette pas ?

(1) Voler le certificat HTTPS de Google
(2) Copier les headers de Google
(3) Patcher Chrome pour désactiver HSTS
