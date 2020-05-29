# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Créations des fichiers de sauvegarde multi serveurs

import discord
import asyncio
import os

async def create_files(message):
    """Fonction chargée de créer les différents fichiers des serveurs.
    Retourne le prefixe du serveur"""

    id_serveur = message.guild.id # Récupération de l'ID du serveur
    id_member = message.author.id # ID de l'utilisateur

    try : #On regarde si les fichiers existent déjà pour le serveur
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt", "r+", encoding="utf-8") #Test Fichier Russian
        text_file.close()

        #-------------------------------------------------------------------------------------
        # Récupération des id et score ["id score", "id score"]
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt","r", encoding="utf-8")
        all_member_rank = text_file.read().split("\n") #Récupération des éléments du fichier
        text_file.close()
        if all_member_rank[-1] == "": #On supprime la ligne vide
            all_member_rank.pop(-1)

        # Division en [[id],[score]]
        member_id_score = [] #Liste membre + score
        for i in range(len(all_member_rank)):
            member_id_score.append(all_member_rank[i].split(" "))

        index = 0
        for i in range (len(member_id_score)):
            if member_id_score[i][0] == str(id_member):
                index = i
                break

        text_file = open("files\\"+str(id_serveur)+"\\rank.txt","w", encoding="utf-8")
        for i in range(len(all_member_rank)):
            if i == index :
                text_file.write(member_id_score[i][0]+" "+str(int(member_id_score[i][1])+1)+"\n")
            else :
                text_file.write(member_id_score[i][0]+" "+member_id_score[i][1]+"\n")
        text_file.close()
        #-------------------------------------------------------------------------------------

        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "r", encoding="utf-8") #Test fichier Prefixe
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
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt","w+", encoding="utf-8")
        text_file.write("False\nFalse\nFalse\nFalse\nFalse\nTrue")
        text_file.close()
        #Fichier Prefixe
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt","w+", encoding="utf-8") #Création du fichier texte
        text_file.write("!")
        text_file.close()
        prefixe = "!"
        #Fichier rank
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt","w+", encoding="utf-8")
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt","a", encoding="utf-8")
        ids = [member.id for member in message.guild.members] #Récupération de tous les ID des membres du serveur
        bots = [member.bot for member in message.guild.members]
        for i in range(len(ids)):
            if bots[i] == False:
                text_file.write(str(ids[i]) + " 0\n") #Ajout de tous les membres dans les fichiers du bot
        text_file.close()
        #Autre fichiers ici
        return prefixe
