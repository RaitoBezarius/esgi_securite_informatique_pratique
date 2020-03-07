# Cours du lundi

## Introduction à ce cours: enjeux, etc

## Premières notions théoriques fondamentales: modèle de menace & surface d'attaque

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
