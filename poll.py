# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Commandes sondages

import discord
import asyncio
from random import choice

async def poll_create(prefixe, message):
    await message.channel.purge(limit=1)
    msg_full = message.content
    msg = msg_full.split(" ")

    if len(msg) == 1 : # Help de la commande
        msg_embed = {
            "color": 16768614, #Couleur de la barre
            "fields": [
                #Zone 1
                {
                "name": choice(ascii_face) + "\n",
                "value": f"""{choix_str}"""
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"
                },
            "title": f"""{question}""",
            "url": "https://arthurtakase.github.io",
            "description": f"""<@{message.author.id}> se pose une question."""
            }
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return

    msg = msg_full.split('//') # On split le message au niveau des divisions

    question = msg[0].split(" ",1)[1] + "\n" #Récupération de la question

    emote = []
    choix = []
    for i in range (1, len(msg)):
        msg_cut = msg[i].split(" ",1)
        if msg_cut[0] == "": #Si l'emote a un espace devant
            while msg_cut[0] == "": #On supprime l'espace
                msg_cut.pop(0)
                msg_cut = msg_cut[0].split(" ",1)

        emote.append(msg_cut[0]) #Récupération des emotes du message .replace(" ", "")
        choix.append(msg_cut[1]) #Récupération des choix du message

    choix_str = ""
    for i in range(len(emote)): #Regroupement du message dans un str
            choix_str += emote[i] +" "+ choix[i] + "\n"

    ascii_face = ["ヾ(•ω•`)o","\(￣︶￣*\))","(*￣3￣)╭","(￣o￣) . z Z","(づ￣ 3￣)づ","o(*￣▽￣*)o","ヽ(✿ﾟ▽ﾟ)ノ","(☞ﾟヮﾟ)☞","(⌐■_■)","o(^▽^)o"]

    msg_embed = {
        "color": 16768614, #Couleur de la barre
        "fields": [
            #Zone 1
            {
            "name": choice(ascii_face) + "\n",
            "value": f"""{choix_str}"""
            }],
        "footer":
            {
            "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
            "text": "Bot by Takase"
            },
        "title": f"""{question}""",
        "url": "https://arthurtakase.github.io",
        "description": f"""<@{message.author.id}> se pose une question."""
        }
    msg_send = await message.channel.send(embed=discord.Embed.from_dict(msg_embed))

    for emoji in emote: #Ajout des réactions au message envoyé
        await msg_send.add_reaction(emoji)
    return
