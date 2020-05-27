# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Help Commandes

import discord
import asyncio

async def help_bot(prefixe, message):
    """Fonction affichant les commandes disponibles dans le bot."""

    msg_embed = {
        "color": 16768614, #Couleur de la barre
        "fields": [
            #Zone 1
            {
            "name": "Personnaliser le bot",
            "value": f"""`{prefixe}prefixe_change`"""
            },
            #Zone 2
            {
            "name": "Misc",
            "value": f"""`{prefixe}help`  `$$$what`"""
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
