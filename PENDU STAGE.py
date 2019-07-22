# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:19:29 2019

@author: tougg
"""

from random import randrange

minuscules = "abcdefghijklmnopqrstuvwxyz "
mots = ["marete", "kewai", "tu sais tu fais rien", "corsini", "hydrophobe", "ornithorynque", "styx", "kiwi", "dictionnaire"]
dessins = [
"""
---------
 |     |
 |
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     o
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |    -+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |    |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |    | |
 |
 |"""]

max_erreurs = len(dessins) - 1

def lire_lettre(propositions):

    """
     Demande une lettre à l'utilisateur en s'assurant qu'elle n'a pas déjà
     été proposée, puis ajoute cette lettre à la liste des lettres déjà
     proposées.
    """

    while True:
        lettre = input("Entrez une proposition de lettre : ")

        if lettre in propositions:
            print("Cette lettre a déjà été proposée.")
        elif lettre not in minuscules or len(lettre) != 1:
            print("Une seule lettre en minuscule, s'il vous plaît.")
        else:
            break;

    propositions.append(lettre)
    return lettre

def mot_avec_tirets(mot, propositions):
    
    """
     Renvoie un mot dont les lettres inconnues sont remplacées par des tirets
    """
    m = ''
    for lettre in mot:
        if lettre in propositions:
            m = m + lettre
        else:
            m = m + '-'
    return m

def partie():
    
    """
     Joue une partie de pendu
     retourne True si gagné, False si perdu
    """

# Initialisations
    erreurs = 0
    mot = mots[randrange(len(mots))]
    propositions = []

# Boucle d'interrogation de l'utilisateur
    print(dessins[erreurs])

    while True:
        print("Lettres déjà proposées :", propositions)
        print("Mot à deviner :", mot_avec_tirets(mot, propositions))

        lettre = lire_lettre(propositions)

        if lettre in mot:
            if mot_avec_tirets(mot, propositions) == mot:
                print("Bravo, vous avez gagné. Le mot était :", mot)
                print("Nombre d'erreurs:", erreurs)
                return True
        else:
            erreurs = erreurs + 1
            print(dessins[erreurs])
            if erreurs >= max_erreurs:
                print("Ah ouais tu sais tu fais rien, le mot était :", mot)
                return False

# Programme principal
print("Salam aleykoum, merci de jouer à mon pendu en python ! ")

parties = 0
victoires = 0


while True:
    parties = parties + 1
    if partie():
        victoires = victoires + 1

    while True:
        cont = input("c pour continuer, a pour arrêter : ")
        if cont == 'c' or cont == 'a':
            break;

    if cont == 'a':
        break;

print("Vous avez joué", parties, "partie(s)")
print("Vous en avez gagné", victoires)
print("Au revoir et merci")
