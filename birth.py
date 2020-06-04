# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Gestion des anniversaires

import discord
import asyncio
import datetime


async def on_file(message):
    """Vérifie si on est déjà dans la liste.
    Retourne True ou False."""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur
    if len(message.content.split(" ")) == 2:
        id = message.mentions[0].id
    else:
        id = message.author.id  # ID de l'utilisateur

    text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "r",
                     encoding="utf-8")  # Test fichier Anniversaire

    is_in = False
    position = 0
    try:
        all_birth_line = text_file.read().split("\n")
        all_birth = []
        for i in range(len(all_birth_line)):
            all_birth.append(all_birth_line[i].split(" "))

        for i in range(len(all_birth)):
            if all_birth[i][0] == str(id):
                is_in = True
                position = i
    except:
        pass

    text_file.close()
    return is_in, position


async def remove_birth(prefixe, message):
    """Supprime un anniversaire des données du serveur.
    Ne retourne rien.
    :prefixe: prefixe des commandes du serveur."""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur

    birth_param = await on_file(message)

    if not birth_param[0]:
        await message.channel.send("pas dans le liste")
        return
    else:
        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "r",
                         encoding="utf-8")  # Test fichier Anniversaire
        all_birth = text_file.read().split("\n")
        text_file.close()

        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "w",
                         encoding="utf-8")  # Test fichier Anniversaire
        for i in range(len(all_birth)):
            if i != birth_param[1]:
                text_file.write(str(all_birth[i]) + "\n")

        text_file.close()

        await message.channel.send("Delet")


async def add_birth(prefixe, message):
    """Ajoute un anniversaire à la base de donnée du serveur.
    Ne retourne rien.
    :prefixe: prefixe des commandes du serveur."""

    id = message.author.id  # Récupération de l'id de l'auteur du message
    id_serveur = message.guild.id  # Récupération de l'ID du serveur

    msg = message.content.split(" ")
    if len(msg) != 4:  # Vérification du nombre d'arguments
        await message.channel.send("pas assez d'arguments.")
        return

    correct_date = False
    try:  # Si la date existe
        day = int(msg[1])
        month = int(msg[2])
        year = int(msg[3])

        if year < 1900:
            correct_date = False
        else:
            date = datetime.datetime(year, month, day)
            correct_date = True

    except:  # Si la date n'existe pas
        await message.channel.send("pas des dates")
        return

    on_file_return = await on_file(message)

    if correct_date and not on_file_return[0]:
        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "a",
                         encoding="utf-8")  # Test fichier Anniversaire
        text_file.write(f"""{id} {day} {month}\n""")
        text_file.close()
        await message.channel.send("date enregistrée")
    else:
        await message.channel.send("non")
