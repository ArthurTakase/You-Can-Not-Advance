# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Commandes Rank

import discord
import asyncio

async def member_id_score_def(message):
    id_serveur = message.guild.id #Récupération de l'ID du serveur

    # Récupération des id et score ["id score", "id score"]
    text_file = open("files\\"+str(id_serveur)+"\\rank.txt","r")
    all_member_rank = text_file.read().split("\n") #Récupération des éléments du fichier
    text_file.close()
    if all_member_rank[-1] == "": #On supprime la ligne vide
        all_member_rank.pop(-1)

    # Division en [[id],[score]]
    member_id_score = [] #Liste membre + score
    for i in range(len(all_member_rank)):
        member_id_score.append(all_member_rank[i].split(" "))

    return member_id_score


async def profil(prefixe, message):
    """Fonction affichant le profil de la personne.
    :prefixe: Prefixe des commandes du serveur.
    Ne retourne rien."""

    id_serveur = message.guild.id #Récupération de l'ID du serveur
    id_member = message.author.id #Récupération de l'ID de l'utilisateur

    member_id_score = await member_id_score_def(message)

    # Si la personne n'est pas dans la liste
    if any(str(id_member) in sub for sub in member_id_score) == False:
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt","a")
        text_file.write(str(id_member) + " 0\n") #On l'ajoute à la base de donnée
        text_file.close()
        member_id_score = await member_id_score_def(message)

    # Optention de l'index de l'utilisateur dans la liste des utilisateurs
    index = 0
    for i in range (len(member_id_score)):
        if member_id_score[i][0] == id_member:
            print(i)
            index = i
            break

    msg_embed = {
        "color": 16768614, #Couleur de la barre
        "thumbnail": {
        "url": f"""{message.author.avatar_url}"""
        },
        "fields": [
            #Zone 1
            {
            "name": "Arrivée sur le serveur",
            "value": f"""{message.author.joined_at.strftime("%d/%m/%Y")}"""
            },
            #Zone 2
            {
            "name": f"""Nombre de message postés depuis le {message.guild.get_member(714964588977979483).joined_at.strftime("%d/%m/%Y")}""",
            "value": f"""{member_id_score[index][1]}"""
            },
            #Zone 3
            {
            "name": f"Niveau",
            "value": f"""{member_id_score[index][1]}"""
            },
            #Zone 4
            {
            "name": f"Anniversaire",
            "value": f"""Faites `{prefixe}addbirth` pour ajouter votre anniversaire à la base de donnée du serveur."""
            }],
        "footer":
            {
            "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
            "text": "Bot by Takase"
            },
        "title": "You Can (Not) Advance",
        "url": "https://arthurtakase.github.io",
        "description": f"""Profil de <@{message.author.id}>"""
        }
    await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
