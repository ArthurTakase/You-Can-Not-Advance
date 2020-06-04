# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Créations des fichiers de sauvegarde multi serveurs

import discord
import asyncio
import os
from rank import *
from math import floor, sqrt


async def create_files(message):
    """Fonction chargée de créer les différents fichiers des serveurs.
    Retourne le prefixe du serveur"""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur
    id_member = message.author.id  # ID de l'utilisateur

    try:  # On regarde si les fichiers existent déjà pour le serveur
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt",
                         "r+", encoding="utf-8")  # Test Fichier Russian
        text_file.close()

        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt",
                         "r", encoding="utf-8")  # Test fichier Prefixe
        param = text_file.read().split("\n")
        text_file.close()

        # -------------------------------------------------------------------------------------
        # Récupération des id et score ["id score", "id score"]
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt", "r", encoding="utf-8")
        all_member_rank = text_file.read().split("\n")  # Récupération des éléments du fichier
        text_file.close()
        if all_member_rank[-1] == "":  # On supprime la ligne vide
            all_member_rank.pop(-1)

        # Division en [[id],[score]]
        member_id_score = []  # Liste membre + score
        for i in range(len(all_member_rank)):
            member_id_score.append(all_member_rank[i].split(" "))

        index = 0
        for i in range(len(member_id_score)):
            if member_id_score[i][0] == str(id_member):
                index = i
                break

        old_level, new_level = 0, 0

        text_file = open("files\\"+str(id_serveur)+"\\rank.txt", "w", encoding="utf-8")
        for i in range(len(all_member_rank)):
            if i == index:
                text_file.write(member_id_score[i][0]+" "+str(int(member_id_score[i][1])+1)+"\n")
            else:
                text_file.write(member_id_score[i][0]+" "+member_id_score[i][1]+"\n")
        text_file.close()

        old_msg = int(member_id_score[index][1])
        level_old = floor(sqrt(old_msg/10))
        msg = int(member_id_score[index][1])+1
        level = floor(sqrt(msg/10))

        if param[1] == "True" and level != level_old:
            msg_embed = {
                "color": 16768614,  # Couleur de la barre
                "thumbnail": {
                    "url": "https://media.discordapp.net/attachments/487002983557627936/717869877599273041/dqzdqdzqdzq.png?width=814&height=683"
                },
                "footer":
                    {
                    "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                    "text": "Bot by Takase"
                },
                "title": "Level UP !",
                "description": f"""<@{message.author.id}> gagne un niveau !"""
            }
            await message.channel.send(embed=discord.Embed.from_dict(msg_embed))

        # -------------------------------------------------------------------------------------
        # Anniversaire
        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "r",
                         encoding="utf-8")  # Test fichier Anniversaire
        text_file.close()
        # Autres fichiers ici
        return param[0]

    except:  # Si les fichiers n'existent pas
        try:  # On essaye de créer le dossier du serveur
            os.mkdir("./files/"+str(id_serveur))
        except:
            pass
        # Fichier Russian
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt", "w+", encoding="utf-8")
        text_file.write("False\nFalse\nFalse\nFalse\nFalse\nTrue")
        # Fichier Prefixe
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "w+",
                         encoding="utf-8")  # Création du fichier texte
        text_file.write("!\nTrue")
        text_file.close()
        prefixe = "!"
        # Fichier Anniversaire
        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "w+",
                         encoding="utf-8")  # Test fichier Anniversaire
        text_file.close()
        # Fichier rank
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt", "w+", encoding="utf-8")
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt", "a", encoding="utf-8")
        # Récupération de tous les ID des membres du serveur
        ids = [member.id for member in message.guild.members]
        bots = [member.bot for member in message.guild.members]
        for i in range(len(ids)):
            if bots[i] == False:
                # Ajout de tous les membres dans les fichiers du bot
                text_file.write(str(ids[i]) + " 0\n")
        text_file.close()
        # Autre fichiers ici
        return prefixe
