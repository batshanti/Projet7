# Projet 7 - Résolvez des problèmes en utilisant des algorithmes en Python

# **AlgoInvest&Trade**
Ce projet contient deux script python visant à maximiser le profit réalisé par les clients après deux ans d'investissement. Le programme devra suggérer une liste des actions les plus rentables à acheter en respectant les contraintes suivantes :
* Chaque action ne peut être achetée qu'une seule fois.
* On ne peut pas acheter une fraction d'action.
* Dépense maximum par client : 500 euros.

Le script **bruteforce.py** fournit un algorithme de force brute qui va tester toutes les combinaisons possible d’investissement. 
Le script **optimized.py**  est une optimisation du premier script visant à réduire le temps d’exécution du programme. Il repose sur un algorithme appelé **Algorithme glouton**.

Nous avons à notre disposition plusieurs jeux de données :
**invest.csv** contenant 20 actions.
**dataset1.csv** et **dataset2.csv** contenant un grand nombre d'actions et ne pouvant être traité par un algorithme de force brute.   

## Installation
#### Dupliquer le projet depuis le dépôt github : 
```
 git clone https://github.com/batshanti/Projet7.git
 cd Projet7/
```
#### Créer un environnement virtuel et l'activer :
(Linux or Mac)
```
 python3 -m venv venv
 source venv/bin/activate
```
(Windows)
```
 py -m venv venv
 env/bin/activate.bat
```
#### Installations des packages :

Les scripts n'utilisent aucune bibliothèques externes.  

## Lancer les scripts
(Linux or Mac)
```
 python3 bruteforce.py
 python3 optimized.py
```
(Windows)
```
python bruteforce.py
python optimized.py
```
**optimized.py** contient un menu pour choisir le jeu de données à utiliser.