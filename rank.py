# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Commandes Rank

import discord
import asyncio
from math import floor, sqrt
from birth import *


async def set_toogle_alert(message):
    """Fonction permettant de désactiver les alertes de montée de niveau des utilisateurs du serveur.
    Ne retourne rien."""

    if message.author.guild_permissions.administrator:  # Si la personne est admin
        id_serveur = message.guild.id  # Récupération de l'ID du serveur

        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt",
                         "r", encoding="utf-8")  # Test fichier Prefixe
        toggle_str = text_file.read().split("\n")
        text_file.close()

        if toggle_str[1] == "True":
            toggle = False
            toggle_str[1] = "False"
            msg_embed = {
                "color": 16768614,  # Couleur de la barre
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/attachments/487002983557627936/717874608723984515/switch-off-icon.png"
                },
                "footer":
                    {
                    "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                    "text": "Bot by Takase"},
                "title": "Les messages de montée de niveau sont maintenant desactivés."
            }
            bot_msg = await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        else:
            toggle = True
            toggle_str[1] = "True"
            msg_embed = {
                "color": 16768614,  # Couleur de la barre
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/attachments/487002983557627936/717874650704773121/switch-on-icon.png"
                },
                "footer":
                    {
                    "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                    "text": "Bot by Takase"},
                "title": "Les messages de montée de niveau sont maintenant activés."
            }
            bot_msg = await message.channel.send(embed=discord.Embed.from_dict(msg_embed))

        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt",
                         "w", encoding="utf-8")  # Test fichier Prefixe
        text_file.write(toggle_str[0] + "\n" + toggle_str[1])
        text_file.close()

        return toggle

    else:
        msg_embed = {
            "color": 6158690,  # Couleur de la barre
            "fields": [
                # Zone 1
                {
                    "name": "Vous n'avez pas les droits",
                    "value": "Pour pouvoir faire cette commande, vous devez être Admin."
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"},
            "title": "Problèmes"
        }
        bot_msg = await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        await bot_msg.delete(delay=4)
        return


async def member_id_score_def(message):
    """Fonction permettant de diviser le fichier rank.txt en une liste propre.
    Retourne une liste [[id, score], [id, score]]"""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur

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

    return member_id_score


async def rank(prefixe, message):
    """Fonction affichant les 3 personnes qui parlent le plus sur le serveur.
    :prefixe: Prefixe du serveur.
    Ne retourne rien."""

    member_id_score = await member_id_score_def(message)

    id_member = message.author.id  # Récupération de l'ID de l'utilisateur

    if len(member_id_score) > 3:

        member_id_score.sort(key=lambda membre: int(membre[1]), reverse=True)

        all_id = []
        for i in range(len(member_id_score)):
            all_id.append(member_id_score[i][0])

        rank_user = all_id.index(str(id_member)) + 1
        dim = "ème"
        if rank_user == 1:
            dim = "er"

        msg_embed = {
            "color": 16768614,  # Couleur de la barre
            "thumbnail": {
                "url": f"""{message.guild.get_member(int(member_id_score[0][0])).avatar_url}"""
            },
            "fields": [
                # Zone 1
                {
                    "name": f"""1er""",
                    "value": f"""**<@{int(member_id_score[0][0])}>** avec {member_id_score[0][1]} messages"""
                },
                # Zone 2
                {
                    "name": f"""2ème""",
                    "value": f"""**<@{int(member_id_score[1][0])}>** avec {member_id_score[1][1]} messages"""
                },
                # Zone 3
                {
                    "name": f"""3ème""",
                    "value": f"""**<@{int(member_id_score[2][0])}>** avec {member_id_score[2][1]} messages"""
                },
                # Zone 4
                {
                    "name": "Votre position",
                    "value": f"""Vous êtes {rank_user}{dim}."""
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"
            },
            "title": "Classement",
            "description": "Les plus actifs du serveur"
        }
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))


async def profil(prefixe, message):
    """Fonction affichant le profil de la personne.
    :prefixe: Prefixe des commandes du serveur.
    Ne retourne rien."""

    msg = message.content.split(" ")

    if len(msg) == 2:
        id_member = message.mentions[0].id
        people = message.mentions[0]
    else:
        id_member = message.author.id  # Récupération de l'ID de l'utilisateur
        people = message.author

    id_serveur = message.guild.id  # Récupération de l'ID du serveur

    member_id_score = await member_id_score_def(message)

    # Si la personne n'est pas dans la liste
    if any(str(id_member) in sub for sub in member_id_score) == False:
        text_file = open("files\\"+str(id_serveur)+"\\rank.txt", "a", encoding="utf-8")
        text_file.write(str(id_member) + " 0\n")  # On l'ajoute à la base de donnée
        text_file.close()
        member_id_score = await member_id_score_def(message)

    # Optention de l'index de l'utilisateur dans la liste des utilisateurs
    index = 0
    for i in range(len(member_id_score)):
        if member_id_score[i][0] == str(id_member):
            index = i
            break

    level = floor(sqrt(int(member_id_score[index][1])/10))

    birth_msg = "`" + str(prefixe) + \
        "addbirth` pour ajouter votre anniversaire à la base de donnée du serveur."

    on_file_return = await on_file(message)
    if on_file_return[0]:  # Si on se trouve dans la liste des anniversaires
        position = on_file_return[1]  # Position dans la liste

        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "r",
                         encoding="utf-8")  # Test fichier Anniversaire

        all_birth_line = text_file.read().split("\n")
        all_birth = []
        for i in range(len(all_birth_line)):
            all_birth.append(all_birth_line[i].split(" "))

        birth_msg = str(all_birth[position][1]) + "/" + str(all_birth[position][2])

    msg_embed = {
        "color": 16768614,  # Couleur de la barre
        "thumbnail": {
            "url": f"""{people.avatar_url}"""
        },
        "fields": [
            # Zone 1
            {
                "name": "Arrivée sur le serveur",
                "value": f"""**{people.joined_at.strftime("%d/%m/%Y")}** (Ouverture du serveur : {message.guild.created_at.strftime("%d/%m/%Y")})"""
            },
            # Zone 2
            {
                "name": f"""Nombre de message postés depuis le {message.guild.get_member(714964588977979483).joined_at.strftime("%d/%m/%Y")}""",
                "value": f"""**{member_id_score[index][1]}**"""
            },
            # Zone 3
            {
                "name": f"Niveau",
                "value": f"""**{level}** (Prochain niveau : {((level+1)**2)*10 - int(member_id_score[index][1])} messages)"""
            },
            # Zone 4
            {
                "name": f"Anniversaire",
                "value": f"""{birth_msg}"""
            }],
        "footer":
            {
            "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
            "text": "Bot by Takase"
        },
        "title": "You Can (Not) Advance",
        "url": "https://arthurtakase.github.io",
        "description": f"""Profil de <@{id_member}>"""
    }
    await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
    return
