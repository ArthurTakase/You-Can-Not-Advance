# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# COmmandes mini jeux nuls

import discord
import asyncio
from random import choice

async def yes_no_ball(prefixe, message):
    """Fonction lançant un 8ball avec interface Json.
    :prefixe: prefixe du serveur
    Ne retourne rien."""

    if len(message.content.split(" ")) != 1 : #Si on pose une question
        #Lecture du fichier avec les reponses
        text_file = open("files\\8ball.txt", "r")
        answer_list = text_file.read().split("\n")
        if answer_list[-1] == "": #Si le dernier élément est vide (merci atom)
            answer_list.pop(-1)

        answer = choice(answer_list) #On choisit une reponse au hasard

        msg_embed = {
            "color": 16768614, #Couleur de la barre
            "thumbnail": {
            "url": "https://cdn.discordapp.com/attachments/487002983557627936/715556628715405352/magic8ball-recto.png"
            },
            "fields": [
                #Zone 1
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

    else : #Help du 8ball
        msg_embed = {
            "color": 6158690, #Couleur de la barre
            "fields": [
                #Zone 1
                {
                "name": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
                "value": "Posez votre question pour enfin connaitre la vérité"
                },
                #Zone 2
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
