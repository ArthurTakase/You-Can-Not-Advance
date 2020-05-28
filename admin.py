# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Commandes administration

#Import lib
import discord
import asyncio

async def clear(prefixe, message):
    """Fonction permettant de clear le channel.
    Ne peux être utilisée que par les administrateurs du serveur.
    :prefixe: prefixe des commandes du serveur.
    Ne retourne rien."""

    if message.author.guild_permissions.administrator : # Si la personne est admin
        msg = message.content.split(" ")
        if len(msg) == 1 : # Help de la commande
            msg_embed = {
                "color": 6158690, #Couleur de la barre
                "fields": [
                    #Zone 1
                    {
                    "name": "Clear",
                    "value": f"""Permet d'effacer des messages du channel. Ne marche que si vous êtes Admin."""
                    },
                    #Zone 2
                    {
                    "name": "Utilisation",
                    "value": f"""`{prefixe}clear [nombre de message à clear]`"""
                    }],
                "footer":
                    {
                    "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                    "text": "Bot by Takase"},
                "title": "Détails de la commande"
                }
            await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
            return

        try :
            limit_clear = int(msg[1]) + 1 #Nombre de message à supprimer (+1 pour delet le message de commande)
            await message.channel.purge(limit=limit_clear) #On supprime les messages
            msg_embed = {
                "color": 16768614, #Couleur de la barre
                "fields": [
                    #Zone 1
                    {
                    "name": "(づ￣ ³￣)づ",
                    "value": f"""{limit_clear-1} messages ont été effacés."""
                    }],
                "footer":
                    {
                    "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                    "text": "Bot by Takase"
                    },
                "title": "Travail Terminé !"
                }
            bot_msg = await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
            await bot_msg.delete(delay = 4)
            return
        except : #Erreur pendant le clear des messages
            msg_embed = {
                "color": 15874618, #Couleur de la barre
                "fields": [
                    #Zone 1
                    {
                    "name": "(╯°□°）╯︵ ┻━┻",
                    "value": "Erreur pendant le clear des messages. Veuillez refaire la commande."
                    }],
                "footer":
                    {
                    "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                    "text": "Bot by Takase"
                    },
                "title": "Error Clear"
                }
            bot_msg = await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
            await bot_msg.delete(delay = 4)
            return

    else : # Si la personne n'est pas admin
        msg_embed = {
            "color": 6158690, #Couleur de la barre
            "fields": [
                #Zone 1
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
        await bot_msg.delete(delay = 4)
        return
