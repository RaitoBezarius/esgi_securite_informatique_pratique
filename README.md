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

# Éléments de références bibliographiques pour aller plus loin

- https://github.com/topics/security
- https://github.com/xairy/linux-kernel-exploitation pour le noyau Linux
- https://github.com/trimstray/the-book-of-secret-knowledge pour une liste assez complète de tout ce qui traîne
- https://www.humblebundle.com/books/cybersecurity-2020-wiley-books des tas de bouquins de sécurité pas cher
- https://www.amazon.com/Windows-Internals-Part-Developer-Reference/dp/0735648735/ pour les internals de Windows
- https://www.alchemistowl.org/pocorgtfo/ - PoC||GTFO, une e-zine de sécurité assez bien foutue
- https://ired.team/ — pour aller plus loin en tant que red teamer, quelques protips
- https://docs.google.com/spreadsheets/d/1b4mUxa6cDQuTV2BPC6aA-GR4zGZi0ooPYtBe4IgPsSc/edit#gid=0 — la C2 Matrix

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

- Scraper sa banque: <https://weboob.org/applications/boobank>
- Dédicace au garçon qui a trop d'ESP32 chez lui: <https://www.thirtythreeforty.net/posts/2019/12/my-business-card-runs-linux/>
- Comment générer des nombres aléatoires correctement: <https://sockpuppet.org/blog/2014/02/25/safely-generate-random-numbers/> ?
- Comment se défendre contre les attaques de replay (c.f. le monsieur avec une trottinette modifiée): <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.69.1965&rep=rep1&type=pdf>
- 2020-03: <https://peterwang512.github.io/CNNDetection/> — détecter des images générés par réseaux de neurones (application à l'anti-deep fakes)
- 2020-03-02: <https://neutrinet.be/fr/blog/collabo>
- 2020-03-02: <https://www.wired.com/story/wireguard-gives-linux-faster-secure-vpn/> (à propos des VPNs)
- 2020-02-28: <https://arxiv.org/abs/2002.12506> — analyse forensics de la télémétrie de Windows pour les diagnostics
- 2020-02-29: <https://mattslifebytes.com/2020/02/29/remote-access-to-production-infrastructure-death-to-the-vpn> — morts aux VPNs (des idées pertinentes, à confronter à la simplicité suprême de WireGuard et sa sécurité).

## Apprendre un peu de Python pratique

Tout d'abord, le tutoriel Python 3.8 est une très bonne référence: <https://docs.python.org/fr/3/tutorial/>

Si vous allez jusqu'à la partie 5, c'est excellent.
Si vous voulez approfondir, allez jusqu'à la partie 9.

On verra la partie 12 ensemble.

Voici un tutoriel plutôt interactif: <https://www.learnpython.org/fr/> qui a l'air décent sur le sujet, il propose d'autres tutoriels eux mêmes, prenez celui qui vous met le plus à l'aise ; on remettra toujours les connaissances à plat ensemble et on reprendra les choses.

# Cours du mardi

## Quelques exercices de Python pour mardi

On va utiliser ce site: <https://adventofcode.com/> assez connu et résoudre les deux premiers en Python, lisez les énoncés à l'avance et venez avec vos questions demain !

Si vous avez faim, nous allons aussi utiliser ce site: <https://www.practicepython.org/> pour pratiquer Python pendant tout le long.

Idéalement, on va essayer de faire 10 exercices d'ici la fin du cours de difficulté variable.

Ceux qui se sentent aventuriers, préparez en un ou deux de votre choix pour demain et on les travaillera ensemble.

## Préparez vos environnements de virtualisation et vos comptes bidons (GMail, PayPal, Facebook par exemple!)

Comme indiqué, on fera une démonstration d'une attaque en utilisant: <http://www.stealmylogin.com/> par exemple.

On ne fera pas du SSL stripping parce qu'on verra des techniques plus puissantes pour contrer HSTS plus tard dans le cours.

## Préparez une installation de Scapy si vous voulez interférer avec le cours (!)

Si vous voulez faire les malins, rien ne vous empêcher d'interférer avec l'attaque, mais laissez moi montrer à vos camarades ce qu'il faut montrer d'abord :-).

## Préparez vos exploits Heartbleed!

Demain, on va tester Heartbleed, si vous ne voulez pas voir et vous voulez tester, allez googler un PoC pour demain !

# Cours du mercredi

## Quelques exercices de Python (à nouveau)

À ceux qui se sentent balèzes, je vous invite à tenter <https://adventofcode.com/> l'exercice 1 puis l'exercice 2.

On essayera de corriger l'exercice 2 entièrement demain (pour la promo où on a fait la première partie de l'exo 2, je vous invite à faire l'exo 1 entièrement et à tenter de faire la 2nde partie de l'exo 2).

Pour du PracticePython, prenez ceux que vous n'avez pas fait encore:

- Exercice 11
- Exercice 20
- Exercice 17
- Exercice 19
- Exercice 16 (attention, générer un mot de passe sécurisé & aléatoire ce n'est pas trivial! Cherchez la notion d'entropie d'un mot de passe et calculez la!)


Vous retrouverez les corrections des exercices qu'on a fait dans le repo, de choses qu'on a abordé, un lien vers la VM « Machine trouée », ce qu'on a utilisé pour Heartbleed et le code de ARP spoofing.

## Un peu de cours technique sur l'attaque & la défense — surfaces d'attaque

On présentera des situations types:

- serveurs SSH ;
- conteneurs Docker ;
- exfiltration par Tor

Par exemple, mais pas que.

## Comment détecter un ARP spoofing en cours?

On va utiliser Scapy pour sniffer les paquets et voir plusieurs contre mesures:

- défense avec cache statique ;
- défense par **statistique** (nombre d'ARP sur un temps donné)

## Outils de DPI: `nfstream`

On va essayer d'analyser du traffic réseau pour détecter ce qui se passe et faire des statistiques.

Vous pouvez réfléchir à des idées de trucs qu'on pourrait analyser:

- les paquets réseaux qui cherchent des Chromecast/appareils AirPlay ;
- les méta-informations qu'on pourrait miner sur les appareils d'un réseau

# Cours du jeudi

## Quelques exercices de Python (mais cette fois ci, on passe à du sérieux)

À ceux qui ont trop de temps libre:

- Tenter <https://projecteuler.net/archives> (les 5 premiers sont sympa, le reste est assez mathématiques)
- Allez mater <https://www.data.gouv.fr/> et trouvez des trucs à faire en Python avec les données
- Mesurez vous sur des compétitions de machine learning (et apprenez le machine learning appliqué): <https://www.kaggle.com/>

### Recette pour la promo du matin

On continue sur PracticePython, ceux que vous n'avez pas fait parmi ceux là :

- Exercice 17
- Exercice 19, qu'on ne corrigera pas en cours, il est le même que le 17
- Exercice 16

Ensuite, on passera sur Advent of Code, le jour 2 de <http://adventofcode.com/>

Puis, si on a assez de temps, on va essayer d'écrire un outil d'archivage de news (avec la librairie `newspaper` sans se casser la tête trop et on fera de l'analyse textuelle avec https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis).

Ou alors, si on a vraiment beaucoup de temps, on écrira une timing attack contre les serveurs qui ne font pas de comparaisons sécurisées (!).

### Recette pour la promo de l'après midi

Pour commencer, on va utiliser l'API de Shodan, allez chopper une clef aussitôt que possible: <https://github.com/achillean/shodan-python>

- Essayez de reproduire les exemples vus en cours relatifs à Shodan ;
- Trouvez des idées intéressantes de requêtes ;
- Faites des statistiques (partielles hélas) de vulnérabilitiés

Ensuite, récupèrez une clef d'API Twitter sur <https://developer.twitter.com/>, faites vous un compte Twitter bidon / poubelle.

On va fabriquer un bot qui RT les hashtags de concours de RTs :-) avec <https://www.tweepy.org/> par exemple.

Si vous avez trop de temps libre, on va faire un algorithme de trading automatisé où on backtestera l'algorithme sur des données de finances, si vous voulez préparer le terrain: <https://www.backtrader.com/home/helloalgotrading/>

Mais ça sera un TP où on va discuter autour de la crypto, et notamment la sécurité des blockchains, etc.

## Phishing moderne & Modlishka: présentation & démonstration

J'espère que vos comptes bidons sont prêts, on va faire du phishing à faible coût et massivement réutilisable.

## Émuler du code de n'importe quelle architecture — Unicorn Engine (depuis Python)

On va jeter un coup d'œil à une version simplifié de cet exemple: <https://github.com/unicorn-engine/unicorn/blob/master/bindings/python/sample_x86.py>

Et on va voir ce qu'on peut faire pour modifier les choses.

## Détecter du shellcode avec Unicorn Engine

On va utiliser ce qu'on a vu juste avant afin de détecter du shellcode, à coupler avec `Scapy` ou `NFStream` pour sniffer et détecter du shellcode sur le réseau.

## Présentation de YARA: https://virustotal.github.io/yara/

## Comment on dissecte du malware? Émulation? Virtualisation? Reverse engineering?

On va voir sur un vrai malware quelques réflexes de ce qu'il faut faire et ce qu'il ne faut pas faire.

# Final cours: cours du vendredi

## Python: Promo du matin (~ 1h)

On essaye d'écrire un malware entier, on discutera `ctypes`, API Windows, détection de malwares Python par les anti-virus, évasion d'antivirus.

## Python: Promo de l'après midi

On passe 30 minutes à regarder ce que vous avez essayé de faire en Python ; et après on passe aux malwares!

## Stéganographie, micro-kernels, manipulateur de CRC & quine: démonstrations & quelques ProTips

- On va regarder le principe de la stégano, pourquoi ça reste d'intérêt aujourd'hui ?
- On va parler des micro-noyaux, qu'est ce que c'est, pourquoi ça vaut le coup de regarder ça aujourd'hui ?
- Manipuler des checksums CRC pour pouvoir obtenir ceux qu'on veut.
- On va discuter des fichiers qui sont à la fois des ZIP, des RAR, des PDF et à peu près tout et n'importe quoi.

## Protocoles anti-censure/anti-DPI (notamment `obfsproxy`) & Command'n'Control modernes

On parlera de C2, ce qu'on veut dans un C2, comment protéger son C2, comment le faire survivre, comment louer son nom de domaine, etc.

On parlera rapidement d'obfs3 et d'obfs2 et leur usage dans Tor.

## Conclusion:

- On reviendra sur des points qu'on aura abordé selon la promo (OSINT, réseaux de neurones, etc.)
- On ouvrira sur des références bibliographiques que vous pouvez vous approprier pour aller plus loin.
- On discutera du projet, je vous donnerai les indications finales relatives à son déroulement (taille de groupe, comment communiquer, mes attentes pour la soutenance.)


On effectuera le QCM à la fin qui sera un PDF sur le repo disponible avant la fin du cours.
