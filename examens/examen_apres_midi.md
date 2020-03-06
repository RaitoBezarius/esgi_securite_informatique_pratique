---
title: QCM de sécurité
author: \textsc{Ryan Lahfa}
advanced-maths: true
advanced-cs: true
---

Indiquez le numéro de chaque réponse que vous estimez être vrai, il peut avoir plusieurs réponses à la même question.

\Question{1} Que faut-il exécuter pour avoir la liste des 100 premiers carrés parfaits (un carré parfait est un entier dont la racine carré est un entier.) en supposant qu'on ait fait `from math import sqrt` avant.

(1) `[x for x in range(100000) if int(sqrt(x)) == sqrt(x)][:100]`
(2) `[x**2 for x in range(10000)][:1000]`
(3) `[x**2 for x in range(100)]`
(4) `[x**2 for x in range(10000)][:1000]`

\Question{2} Si on dispose de malware, mettez dans l'ordre les meilleures solutions pour le reverse engineer:

(1) Le virtualiser?
(2) Le containerizer?
(3) L'émuler ?
(4) Le mettre sur une machine à part qu'on jettera après

\Question{3} Si on utilise Meltdown pour lire la RAM de notre voisin de machine virtuelle (imaginez un EC2 sur un cloud AWS), que pourrait-t-il se passer ?

(1) On pourrait pouvoir obtenir la clef SSH du serveur à côté
(2) On pourrait obtenir le mot de passe de la base de données
(3) On pourrait exécuter du code à distance

\Question{4} Que fait `requests.get('https://google.fr')` ?

(1) Ouvre un navigateur et lance la requête HTTP pour `GET` <https://google.fr>
(2) Fait une requête HTTP `GET` directement <https://google.fr>
