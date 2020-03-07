# (Vrai) cours de sécurité pratique

Vous retrouverez ici tous les contenus de cours produits pour le cours de sécurité à l'ESGI:

- slides ;
- plan du cours & avancement par promo ;
- ressources en vrac ;
- idées de projets ;
- QCMs & corrigés ;
- et d'autres choses

N'hésitez pas à me demander par email ou ouvrir une issue pour poser des questions ou demander des précisions.

Si vous voulez contribuer à ce référentiel, cela sera avec plaisir :).

# Ressources pour un environnement de développement en béton armé

- Visual Studio Code est assez excellent si vous voulez un éditeur simple et bien foutu
- PyCharm édition pro est l'IDE poids lourd, il est gratuit pour les étudiants

Pour le reste, si vous ne l'avez toujours pas fait, dépêchez vous d'aller redeem le <https://education.github.com/pack> — il contient des tas de goodies (payant souvent) qui sont gratuits pour vous! (Dont tous les IDE de JetBrains gratuit tant que vous êtes étudiants!!)

# Éléments de références bibliographiques pour aller plus loin

- Cours de RE bien stylé: <https://class.malware.re/> (!!!)
- Android pour iPhone: <https://projectsandcastle.org/>
- https://github.com/topics/security
- https://github.com/xairy/linux-kernel-exploitation pour le noyau Linux
- https://github.com/trimstray/the-book-of-secret-knowledge pour une liste assez complète de tout ce qui traîne
- https://www.humblebundle.com/books/cybersecurity-2020-wiley-books des tas de bouquins de sécurité pas cher
- https://www.amazon.com/Windows-Internals-Part-Developer-Reference/dp/0735648735/ pour les internals de Windows
- https://www.alchemistowl.org/pocorgtfo/ - PoC||GTFO, une e-zine de sécurité assez bien foutue
- https://ired.team/ — pour aller plus loin en tant que red teamer, quelques protips
- https://docs.google.com/spreadsheets/d/1b4mUxa6cDQuTV2BPC6aA-GR4zGZi0ooPYtBe4IgPsSc/edit#gid=0 — la C2 Matrix
- 

# Idées de projets (annuels peut-être?)

## DevSecOps (tmtc Quentin)

- Contribuer à <https://github.com/aquasecurity/kube-hunter> c'est un tournant intéressant, c'est un petit outil Python simple à comprendre, qui a énormément de potentiel ;

## Honeypots

- Fabriquer un honeypot Docker: faire croire qu'on est un serveur Docker et attraper les réponses et faire croire que l'ennemi a un shell, vous pouvez vous inspirer de: <https://github.com/lnslbrty/potd>
- Techniques anti-honeypot: comment trouver des facteurs / invariants qu'on ne peut trouver que des vraies machines ? (tester le timing de certains opérations CPU, des instructions spéciales ? AVX, etc.)
- Détecter <frida.re> et empêcher sa détection
- Honeypot pour PostgreSQL

## Fuzzing

- Faire un fuzzer du protocole IMAP/POP3 ou fuzzer le protocole avec un truc comme AFL, honggfuzz, Peach Fuzzer, etc ;
- Faire du fuzzing "structure-aware" avec https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md par exemple ;
- Tirer une base de données des crashs en scrapant les workers d'OSS Fuzz: https://github.com/google/oss-fuzz (pour trouver des 0days avant tout le monde)
- Fuzzer les implémentations de JSON Web Tokens (JWT) à la recherche d'un nouveau Heartbleed :-)
- Fuzzer le protocole de Discord (surtout côté appels) à la recherche de bug ou de 0days :-).
- Fuzzer CS:GO pour trouver des 0days: oui, y a des gens qui font ça https://blog.firosolutions.com/exploits/counter-strike-go/ (remplacez CS:GO par votre jeu préféré et ça marche aussi.)

## Reverse engineering

- Prendre une appliance type VPN (FortiNet, Citrix, Pulse Secure) sous forme de VM et mettre à plat son fonctionnement entièrement (attention, ça requiert des bonnes compétences en système, rien que parce que les appliances sont protégés et vont vous demander de pwner le full disk encryption en choppant la RAM de la VM ou en étant plus créatif)

## OSINT

- Un bot qui cherche des informations sur nous et nous alerte sur des leak potentiels de notre vie privée (cherchez sur Twitter pour des mots clefs personnels, scrapper Google, utiliser theHarvester mais dans l'autre sens)
- Un bot Discord qui rejoint autant de serveurs que possible pour fabriquer un mapping entre les pseudos et les serveurs et surveiller discrètement une/des cibles sur plein de serveurs.

## Réseau

- Fabriquer un outil pour déployer un VPN avec redirection de traffic vers un bridge qui fait tourner un `tcpdump` pour stocker les trames (à utiliser avec `mitmproxy` et WireGuard) automatiquement.
- Module Python pour pouvoir lancer plusieurs requêtes parallèles avec plusieurs circuits Tor (pensez `multitor` dans Python automatisé).
- Module Python pour ne communiquer qu'en IPv6 (pensez évasion d'IDS/IPS débiles)
- Utiliser la sortie de nmap pour faire du reporting et de l'analyse avancée, style https://github.com/SabyasachiRana/WebMap
- Utiliser eBPF pour faire de la sécurité avancée dans un contexte Kubernetes/Docker: https://github.com/cilium/cilium
- Utiliser https://github.com/swisskyrepo/PayloadsAllTheThings pour écrire un testeur de quelque chose (XSS, OAuth, SAML, race conditions, etc.)
- Écrire un testeur de timing attacks avancé
- Analyser le protocole 4G et chercher des vulnérabilités!

## Cryptomonnaie

- Analyse de transactions et retraçage de l'origine d'une transaction
- Analyse de blanchiement de sous-sous

## Dissection

Dissecter des protocoles propriétaires:

- Appels/Messages WhatsApp
- Appels/Messages Messenger
- Snapchat
- Apps d'achat dans les (super)marchés: Casino Max (€€€), Carrefour, whatever
- Startups à la con qui font du B2C sur Paris (Uber, AirBnb, Deliveroo, Franprix, G7, Doctolib, Affluences, Amazon Shopping)
- Apps de miles des compagnies aériennes: Air France, etc.

## Mobile

- Chasser des 0days dans des applications bancaires ou vraiment ce que vous voulez
- Fabriquer un malware Android user-space
- (plus dur) Fabriquer un malware Android au niveau kernel (vous allez avoir besoin de beaucoup de ressources / temps et de patience!)

## Système

- Écrire un rootkit kernel pour Windows
- Écrire un rootkit kernel pour Linux
- Écrire des modules Apache backdoor (vous droppez une DLL/une lib dans les modules Apache, puis vous l'activez et ça vous permet d'avoir tjrs un accès SSH détourné, indétectable tant qu'on audite pas ses modules, qui fait ça d'ailleurs ?)
- Écrire des modules PHP backdoor
- Écrire des modules Python backdoor
- Écrire un outil pour automatiquement backdoorer une codebase discrètement (JavaScript, PHP, Python, ce que vous voulez)
- Écrire un outil pour backdoorer un serveur web pour envoyer le traffic TLS vers un autre serveur, discretos bien sûr

## Outillage

- Écrire un daemon de logging avec une belle interface web sans avoir à utiliser toute la stack ELK (un truc plus léger)
- Bot Twitter qui détecte les trends en infosec et vous envoie un email ou whatever.

# Machines virtuelles

La « Machine trouée »: <https://www.vulnhub.com/entry/bwapp-bee-box-v16,53/> — configurez la avec un réseau bridgé et un host-only pour pouvoir faire des choses avec tranquillement. Si vous avez du mal, pingez moi !

# News du monde de la sécurité informatique / Veille active

**NEW** :
- Mars 2020: <https://blog.cryptographyengineering.com/2020/03/06/earn-it-is-an-attack-on-encryption/> — nouvelle loi anti crypto dans les cartons aux USA
- Mars 2020: <https://duo.com/blog/the-beer-drinkers-guide-to-saml> — SAML, le nouveau truc à péter
- Mars 2020: <http://blog.ptsecurity.com/2020/03/intelx86-root-of-trust-loss-of-trust.html> — peut-être, adieu Intel Management Engine?
- Mars 2020: <https://pythonspeed.com/articles/dont-need-kubernetes/> — pourquoi il faut ne pas utiliser Kubernetes?
- Mars 2020: Hacker News qui kiffe `nfstream`: <https://news.ycombinator.com/item?id=22488470>

**OLD** :
- Scraper sa banque: <https://weboob.org/applications/boobank>
- Dédicace au garçon qui a trop d'ESP32 chez lui: <https://www.thirtythreeforty.net/posts/2019/12/my-business-card-runs-linux/>
- Comment générer des nombres aléatoires correctement: <https://sockpuppet.org/blog/2014/02/25/safely-generate-random-numbers/> ?
- Comment se défendre contre les attaques de replay (c.f. le monsieur avec une trottinette modifiée): <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.69.1965&rep=rep1&type=pdf>
- 2020-03: <https://peterwang512.github.io/CNNDetection/> — détecter des images générés par réseaux de neurones (application à l'anti-deep fakes)
- 2020-03-02: <https://neutrinet.be/fr/blog/collabo>
- 2020-03-02: <https://www.wired.com/story/wireguard-gives-linux-faster-secure-vpn/> (à propos des VPNs)
- 2020-02-28: <https://arxiv.org/abs/2002.12506> — analyse forensics de la télémétrie de Windows pour les diagnostics
- 2020-02-29: <https://mattslifebytes.com/2020/02/29/remote-access-to-production-infrastructure-death-to-the-vpn> — morts aux VPNs (des idées pertinentes, à confronter à la simplicité suprême de WireGuard et sa sécurité).

# Apprendre un peu de Python pratique

Tout d'abord, le tutoriel Python 3.8 est une très bonne référence: <https://docs.python.org/fr/3/tutorial/>

Si vous allez jusqu'à la partie 5, c'est excellent.
Si vous voulez approfondir, allez jusqu'à la partie 9.

Voici un tutoriel plutôt interactif: <https://www.learnpython.org/fr/> qui a l'air décent sur le sujet, il propose d'autres tutoriels eux mêmes, prenez celui qui vous met le plus à l'aise ; on remettra toujours les connaissances à plat ensemble et on reprendra les choses.
