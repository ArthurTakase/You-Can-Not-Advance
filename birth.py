# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Gestion des anniversaires

import discord
import asyncio
import datetime
from glob import glob


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


async def is_birth_today():
    """Regarde Si il y a un anniversaire aujourd'hui.
    Retourne True et les IDs OU False et un élément vide."""

    all_id = [""]

    # all guild id
    for i in range(len(glob("./files/*/"))):
        id_serveur = glob("./files/*/")[i].split("\\")[1]  # Récupération de l'ID du serveur

        # Get id channel serveur
        text_file = open("files\\"+str(id_serveur)+"\\param_bot.txt", "r",
                         encoding="utf-8")  # Test fichier Anniversaire
        id_channel = text_file.read().split("\n")[2]
        text_file.close()

        # Récupération de la date du jour
        current_day = int(str(datetime.date.today()).split("-")[2])
        current_month = int(str(datetime.date.today()).split("-")[1])

        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "r",
                         encoding="utf-8")  # Test fichier Anniversaire

        # Lecture du fichier des anniversaires
        all_birth_line = text_file.read().split("\n")
        all_birth = []
        for i in range(len(all_birth_line)):
            all_birth.append(all_birth_line[i].split(" "))
        all_birth.pop(-1)

        for i in range(len(all_birth)):
            if int(all_birth[i][1]) == current_day and int(all_birth[i][2]) == current_month:
                all_id.append("True " + str(all_birth[i][0]) + " " + str(id_channel))

    all_id.pop(0)

    if len(all_id) != 1:
        return all_id
    else:
        return all_id


async def next_birth(prefixe, message):
    """Donne le prochain anniversaire de la Liste.
    Ne retourne rien.
    :prefixe: prefixe des commandes du serveur."""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur

    text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "r",
                     encoding="utf-8")  # Test fichier Anniversaire

    # Récupération de la date du jour
    current_day = int(str(datetime.date.today()).split("-")[2])
    current_month = int(str(datetime.date.today()).split("-")[1])

    # Récupération des anniversaires et des ID
    all_birth_line = text_file.read().split("\n")
    all_birth = []
    for i in range(len(all_birth_line)):
        all_birth.append(all_birth_line[i].split(" "))
    all_birth.pop(-1)  # On supprime l'élément vide de la liste
    text_file.close()

    # Tri des anniversaires dans le bon ordre
    all_date = []
    for i in range(len(all_birth)+1):
        if i != len(all_birth):  # Ajout de tous les anniversaires
            all_date.append("2002-" + str(all_birth[i][2]) + "-" + str(all_birth[i][1]))
        else:  # Ajout de la date du jour comme repère
            all_date.append("2002-" + str(current_month) + "-" + str(current_day))
    all_date.sort()

    # Detection de l'index du jour dans la liste
    index = 0  # Emplacement du prochain anniversaire
    for i in range(len(all_date)):
        if all_date[i] == "2002-" + str(current_month) + "-" + str(current_day):
            index = i + 1
    if index >= len(all_date):  # Si index est le dernier élément de la liste
        index -= len(all_date)-1

    # Date du prochain anniversaire
    next_day = all_date[index].split("-")[2]
    next_month = all_date[index].split("-")[1]

    # id du prochain anniversaire
    next_id = ""
    for i in range(len(all_birth)):
        if all_birth[i][1] == next_day and all_birth[i][2] == next_month:
            next_id = all_birth[i][0]

    msg_embed = {
        "color": 16768614,  # Couleur de la barre
        "fields": [
            # Zone 1
            {
                "name": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
                "value": f"""<@{next_id}> le **{next_day}/{next_month}**."""
            }],
        "thumbnail": {
            "url": f"""{message.guild.get_member(int(next_id)).avatar_url}"""
        },
        "footer":
            {
            "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
            "text": "Bot by Takase"},
        "title": "Prochain anniversaire"
    }
    bot_msg = await message.channel.send(embed=discord.Embed.from_dict(msg_embed))


async def remove_birth(prefixe, message):
    """Supprime un anniversaire des données du serveur.
    Ne retourne rien.
    :prefixe: prefixe des commandes du serveur."""

    id_serveur = message.guild.id  # Récupération de l'ID du serveur

    birth_param = await on_file(message)

    if not birth_param[0]:
        await message.channel.send("pas dans la liste")
        return
    else:
        text_file = open("files\\"+str(id_serveur)+"\\birth.txt", "r",
                         encoding="utf-8")  # Test fichier Anniversaire
        all_birth = text_file.read().split("\n")[:-1]
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
