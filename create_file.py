# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Créations des fichiers de sauvegarde multi serveurs

import discord
import asyncio
import os

async def create_files(message):
    """Fonction chargée de créer les différents fichiers des serveurs.
    Retourne le prefixe du serveur"""

    id_serveur = message.guild.id #Récupération de l'ID du serveur

    try : #On regarde si les fichiers existent déjà pour le serveur
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt", "r+") #Test Fichier Russian
        text_file.close()
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt", "r") #Test Fichier Rank
        #Ajout d'un message au compteur
        text_file.close()
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "r") #Test fichier Prefixe
        prefixe = text_file.read().split("\n")
        text_file.close()
        #Autres fichiers ici
        return prefixe[0]

    except : #Si les fichiers n'existent pas
        try :  #On essaye de créer le dossier du serveur
            os.mkdir("./files/"+str(id_serveur))
        except :
            pass
        #Fichier Russian
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt","w+")
        text_file.write("False\nFalse\nFalse\nFalse\nFalse\nTrue")
        text_file.close()
        #Fichier Prefixe
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt","w+") #Création du fichier texte
        text_file.write("!")
        text_file.close()
        prefixe = "!"
        #Fichier rank
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt","w+")
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt","a")
        ids = [member.id for member in message.guild.members] #Récupération de tous les ID des membres du serveur
        for i in range(len(ids)):
            text_file.write(str(ids[i]) + " 0\n") #Ajout de tous les membres dans les fichiers du bot
        text_file.close()
        #Autre fichiers ici
        return prefixe
