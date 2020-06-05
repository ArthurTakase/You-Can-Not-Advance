# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Commandes Edit Bot

import discord
import asyncio
import os


async def prefixe_show(prefixe, message):
    """Fonction qui donne le préfixe du serveur dans un message embed.
    :prefixe: prefixe du serveur
    Ne retourne rien."""

    msg_embed = {
        "color": 6158690,
        "fields": [{
            "name": "Préfixe",
            "value": f"""Le préfixe pour ce serveur est `{prefixe}`.
            Pour changer de préfixe faite la commande `{prefixe}prefixechange`.
            Tapez `{prefixe}help` pour afficher toutes les commandes."""}],
        "footer": {
            "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
            "text": "Bot by Takase"
        }
    }
    await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
    return


async def prefixe_change(prefixe, message):
    """Fonction permettant de changer le le préfixe du bot.
    :prefixe: prefixe du serveur
    Ne retourne rien."""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur
    msg = message.content.split(" ")

    if len(msg) == 1:
        msg_embed = {
            "color": 6158690,  # Couleur de la barre
            "fields": [
                # Zone 1
                {"name": "Edit Préfixe",
                 "value": "Permet d'éditer le préfixe des commandes pour le serveur."},
                # Zone 2
                {"name": "Utilisation",
                 "value": f"""`{prefixe}prefixechange [nouveau préfixe]`"""}],
            "footer": {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"},
            "title": "Détails de la commande"
        }
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return

    try:  # On regarde si le fichier "param_bot.txt" existe déjà pour le serveur
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "r")
        prefixe = text_file.read().split("\n")
    except:
        msg_embed = {
            "color": 16768614,  # Couleur de la barre
            "fields": [
                {"name": "Edit Préfixe",
                 "value": "Initialisation des fichiers. Veuillez refaire la commande."}]}
        # "Initialisation des fichiers. Veuillez refaire la commande.")
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return

    if prefixe[0] == msg[1]:
        msg_embed = {
            "color": 16768614,  # Couleur de la barre
            "fields": [
                # Zone 1
                {
                    "name": "¯\_(ツ)_/¯",
                    "value": f"""le préfixe `{prefixe[0]}` est déjà en place sur le serveur."""
                }],
            "footer":
                {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"
            },
            "title": "On radote ?"
        }
        # -----------------------------------------------------------------
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return
    else:
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "w")
        text_file.write(msg[1] + "\n" + prefixe[1])
        msg_embed = {
            "color": 16768614,  # Couleur de la barre
            "fields": [
                # Zone 1
                {"name": "Préfixe édité avec succès !",
                 "value": f"""Nouveau préfixe pour le serveur : `{msg[1]}`."""}],
            "footer": {
                "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                "text": "Bot by Takase"}}
        await message.channel.send(embed=discord.Embed.from_dict(msg_embed))
        return
