# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Commandes mini jeux nuls

import discord
import asyncio
from random import choice


async def yes_no_ball(prefixe, message):
    """Fonction lançant un 8ball avec interface Json.
    :prefixe: prefixe du serveur
    Ne retourne rien."""

    if len(message.content.split(" ")) != 1:  # Si on pose une question
        # Lecture du fichier avec les reponses
        text_file = open("files\\8ball.txt", "r", encoding="utf-8")
        answer_list = text_file.read().split("\n")
        text_file.close()
        if answer_list[-1] == "":  # Si le dernier élément est vide (merci atom)
            answer_list.pop(-1)

        answer = choice(answer_list)  # On choisit une reponse au hasard

        msg_embed = {
            "color": 16768614,  # Couleur de la barre
            "thumbnail": {
                "url": "https://cdn.discordapp.com/attachments/487002983557627936/715556628715405352/magic8ball-recto.png"
            },
            "fields": [
                # Zone 1
                {
                    "name": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
                    "value": f"""{answer}"""
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"
            },
            "title": "Magic 8 Ball",
        }
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return

    else:  # Help du 8ball
        msg_embed = {
            "color": 6158690,  # Couleur de la barre
            "fields": [
                # Zone 1
                {
                    "name": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
                    "value": "Posez votre question pour enfin connaitre la vérité"
                },
                # Zone 2
                {
                    "name": "Utilisation",
                    "value": f"""`{prefixe}8ball [question] ?`"""
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"
            },
            "title": "Magic 8 Ball"
        }
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return


async def russian(prefixe, message):
    """Fonction permettant de jouer à la roulette russe sur Discord.
    :prefixe: prefixe du serveur.
    Ne retourne rien"""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur

    text_file = open("files\\"+str(id_serveur)+"\\russian.txt", "r", encoding="utf-8")
    # Récupération de ce qui se trouve dans le fichier Russian.txt
    russian_text = text_file.read().split("\n")
    text_file.close()
    if russian_text[-1] == "":  # Si la dernière ligne est vide
        russian_text.pop(-1)

    answer = choice(russian_text)  # Récupération d'un élément au hasard

    gif_true = ["https://media.giphy.com/media/10ZuedtImbopos/giphy.gif",  # Gif si on perd
                "https://media.giphy.com/media/12MgUpnxEq3ypy/giphy.gif",
                "https://media.giphy.com/media/RCwOTgJidoMda/giphy.gif",
                "https://thumbs.gfycat.com/ClearcutCommonBalloonfish-size_restricted.gif",
                "https://media.giphy.com/media/brjQAYiFPBpWE/giphy.gif",
                "https://media.giphy.com/media/l2Je0fLka7iFCQ9Gg/giphy.gif"]
    gif_false = ["https://media.giphy.com/media/55SfA4BxofRBe/giphy.gif",  # Gif si on échappe à la mort
                 "https://media.giphy.com/media/QA88yMhazfDI4/giphy.gif",
                 "https://media.giphy.com/media/22irWwDRbas8w/giphy.gif",
                 "https://media.giphy.com/media/C1m9MPACd6Nk4/giphy.gif",
                 "https://media.giphy.com/media/i3RISPULnoyD9QHsJF/giphy.gif",
                 "https://media.giphy.com/media/YrqdBJsEch54df9Iiy/giphy.gif"]

    if answer == "True":  # La balle est partie
        msg_embed = {
            "color": 16727357,  # Couleur de la barre
            "image": {
                "url": choice(gif_true)
            },
            "fields": [
                # Zone 1
                {
                    "name": "Vous avez perdu...",
                    "value": f"""C'est l'heure de mourir pour <@{message.author.id}>."""
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"
            },
            "title": "PAN !"
        }
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        # Réécriture des valeurs de Russian.txt
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt", "w+")
        text_file.write("False\nFalse\nFalse\nFalse\nFalse\nTrue")
        text_file.close()
    else:
        msg_embed = {
            "color": 6158690,  # Couleur de la barre
            "image": {
                "url": choice(gif_false)
            },
            "fields": [
                # Zone 1
                {
                    "name": "Vous avez de la chance",
                    "value": f"""Votre heure n'est pas encore venue <@{message.author.id}>.
                Il reste {len(russian_text)-1} tirs..."""
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"
            },
            "title": "Pouf..."
        }
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        # Suppression d'un False dans Russian.txt
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt", "w+")
        text_file.write("False\n"*(russian_text.count("False")-1)+"True")
        text_file.close()
