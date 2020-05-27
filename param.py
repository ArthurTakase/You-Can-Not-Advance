# You Can (Not) Advance (You're (Not) Alone 2.0)
# Authour : Takase
# Edit Bot Commandes

import discord
import asyncio
import os


async def prefixe_file(message):
    """Fonction créant les dossiers"""

    id_serveur = message.guild.id #Récupération de l'ID du serveur

    try : #On regarde si le fichier "param_bot.txt" existe déjà pour le serveur
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "r")
        prefixe = text_file.read().split("\n")
        return prefixe[0]
    except : #Si le fichier existe, on le crée
        try :  #On essaye de créer le dossier du serveur
            os.mkdir("./files/"+str(id_serveur))
        except :
            pass
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt","w+") #Création du fichier texte
        text_file.write("!")
        prefixe = "!"

        return prefixe


async def prefixe_show(prefixe, message):
    """Fonction qui donne le préfixe du serveur dans un message embed."""

    msg_embed = {
        "color": 16768614,
        "fields": [{
            "name": "Préfixe",
            "value": f"""Le préfixe pour ce serveur est `{prefixe}`.
            Pour changer de préfixe faite la commande `{prefixe}prefixe_change`.
            Tapez `{prefixe}help` pour afficher toutes les commandes."""}],
        "footer": {
            "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
            "text": "Bot by Takase"
        }
    }
    await message.channel.send(embed=discord.Embed.from_dict(msg_embed))


async def prefixe_change(prefixe, message):
    """Fonction permettant de changer le le préfixe du bot."""

    id_serveur = message.guild.id #Récupération de l'ID du serveur
    msg = message.content.split(" ")

    if len(msg) == 1 :
        msg_embed = {
            "color": 16768614, #Couleur de la barre
            "fields": [
                #Zone 1
                {"name": "Edit Préfixe",
                "value": "Permet d'éditer le préfixe des commandes pour le serveur."},
                #Zone 2
                {"name": "Utilisation",
                "value": f"""{prefixe}prefixe_change [nouveau préfixe]"""}],
            "footer": {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"}}
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return

    try : #On regarde si le fichier "param_bot.txt" existe déjà pour le serveur
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "r")
        prefixe = text_file.read().split("\n")
    except :
        msg_embed = {
            "color": 16768614, #Couleur de la barre
            "fields": [
                {"name": "Edit Préfixe",
                "value": "Initialisation des fichiers. Veuillez refaire la commande."}]}
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))#"Initialisation des fichiers. Veuillez refaire la commande.")
        return

    if prefixe[0] == msg[1] :
        await message.channel.send("Le préfixe que vous voulez mettre est déjà en place sur ce serveur.")
        return
    else :
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "w")
        text_file.write(msg[1])
        msg_embed = {
            "color": 16768614, #Couleur de la barre
            "fields": [
                #Zone 1
                {"name": "Préfixe édité avec succès !",
                "value": f"""Nouveau préfixe pour le serveur : `{msg[1]}`."""}],
            "footer": {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"}}
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return
