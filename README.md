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

# Machines virtuelles

La « Machine trouée »: <https://www.vulnhub.com/entry/bwapp-bee-box-v16,53/> — configurez la avec un réseau bridgé et un host-only pour pouvoir faire des choses avec tranquillement. Si vous avez du mal, pingez moi !

# News du monde de la sécurité informatique / Veille active

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
