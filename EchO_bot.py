#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '807308900:AAHr0Zzd4-_zS9NOa9JuAMMpOgh4Btyo5Vk'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/pendu'
@bot.message_handler(commands=['pendu', 'start'])
def send_welcome(message):
    bot.reply_to(message, main(message))
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

def lire_lettre(propositions,message):

    """
     Demande une lettre à l'utilisateur en s'assurant qu'elle n'a pas déjà
     été proposée, puis ajoute cette lettre à la liste des lettres déjà
     proposées.
    """

    while True:
        lettre=message.text
        # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
        # @bot.message_handler(func=lambda message: True)
        # def echo_message(message): 
        #     bot.reply_to(message, message.text)
        #     lettre = input("Entrez une proposition de lettre : ")

        if lettre in propositions:
            bot.reply_to(message,str("Cette lettre a déjà été proposée."))
        elif lettre not in minuscules or len(lettre) != 1:
            bot.reply_to(message,str("Une seule lettre en minuscule, s'il vous plaît."))
        else:
            break

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

def partie(message):
    
    """
     Joue une partie de pendu
     retourne True si gagné, False si perdu
    """

# Initialisations
    erreurs = 0
    mot = mots[randrange(len(mots))]
    propositions = []

# Boucle d'interrogation de l'utilisateur
    bot.reply_to(message,str(dessins[erreurs]))

    while True:
        bot.reply_to(message,str("Lettres déjà proposées :") + str(propositions))
        bot.reply_to(message, mot_avec_tirets(mot, propositions))

        lettre = lire_lettre(propositions,message)

        if lettre in mot:
            if mot_avec_tirets(mot, propositions) == mot:
                bot.reply_to(message,str("Bravo, vous avez gagné. Le mot était :", mot))
                bot.reply_to(message,str("Nombre d'erreurs:", erreurs))
                return True
        else:
            erreurs = erreurs + 1
            bot.reply_to(message,str(dessins[erreurs]))
            if erreurs >= max_erreurs:
                bot.reply_to(message,str("Ah ouais tu sais tu fais rien, le mot était :", mot))
                return False


def main(message):
    # Programme principal
    bot.reply_to(message,str('Salam aleykoum, merci de jouer à mon pendu en python ! '))
    parties = 0
    victoires = 0
    while True:
        parties = parties + 1
        if partie(message):
            victoires = victoires + 1

        while True:
            cont = input("c pour continuer, a pour arrêter : ")
            if cont == 'c' or cont == 'a':
                break

        if cont == 'a':
            break

    bot.reply_to(message,str('Vous avez joué', parties, 'partie(s)'))
    bot.reply_to(message,str('Vous en avez gagné', victoires))
    bot.reply_to(message,str('Au revoir et merci'))


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message): 
#     bot.reply_to(message, message.text)


bot.polling()