# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Commandes Help

import discord
import asyncio


async def help_bot(prefixe, message):
    """Fonction affichant les commandes disponibles dans le bot.
    :prefixe: prefixe du serveur
    Ne retourne rien."""

    msg_embed = {
        "color": 6158690,  # Couleur de la barre
        "fields": [
            # Zone 1
            {
                "name": "Personnaliser le bot",
                "value": f"""`{prefixe}prefixechange`"""
            },
            # Zone 2
            {
                "name": "Misc",
                "value": f"""`$$$what`   `{prefixe}help`  `{prefixe}poll`  `{prefixe}8ball`  `{prefixe}russian`"""
            },
            # Zone 3
            {
                "name": "Administration",
                "value": f"""`{prefixe}clear`"""
            },
            # Zone 4
            {
                "name": "Niveaux et Profils",
                "value": f"""`{prefixe}profile`  `{prefixe}rank`  `{prefixe}alert`"""
            },
            # Zone 5
            {
                "name": "Anniversaires",
                "value": f"""`{prefixe}addbirth`  `{prefixe}removebirth`  `{prefixe}nextbirth`"""
            }],
        "footer":
            {
            "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
            "text": "Bot by Takase"
        },
        "title": "You Can (Not) Advance",
        "url": "https://arthurtakase.github.io",
        "description": "Un magnifique bot discord qui peut tout faire !"
    }
    await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
    return
