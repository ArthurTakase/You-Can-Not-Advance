# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Fichier principal

# Import lib
import discord
import asyncio
from random import choice, randint
import datetime
# Import local files
from param import *
from help import *
from private_code import *
from poll import *
from game import *
from admin import *
from rank import *
from create_file import *
from birth import *

TOKEN = get_token()  # Modifier get_token() par votre Token

# Variables gloables
nbr_msg = 0
is_birth = False

# Objet bot


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.is_birthday())

    async def is_birthday(self):
        """Fonction regardant si il y a un anniversaire ce jour.
        Ne retourne rien."""

        global is_birth

        await self.wait_until_ready()
        while not self.is_closed():
            return_birth = await is_birth_today()
            index = len(return_birth)

            for i in range(index):
                all = return_birth[i].split(" ")
                print(all)
                channel = self.get_channel(int(all[2]))  # channel ID goes here

                if all[0] == "True":  # Si il y a un anniversaire
                    await channel.send("<@" + str(all[1]) + ">")  # Envoyer le message
                else:  # Si il n'y a pas d'anniversaire
                    await channel.send("no")

            await asyncio.sleep(1)  # Attendre 24h

    async def set_status(self):
        """Fonction permettant de changer de status du bot tous les x messages"""

        global nbr_msg
        list = [["Kingdom hearts", "Witcher 3"],  # Game
                ["Parasyte", "Evangelion"],  # Regarde
                ["twenty one pilots", "Queen"],  # Ecoute
                ["le $$$what", "la puissance"]]  # Streame

        if nbr_msg - 99 == 0:  # Nombre de message à poster -1
            type = randint(0, 3)
            if type == 0:  # Joue à
                await client.change_presence(activity=discord.Game(name=choice(list[0])))
            elif type == 1:  # Regarde
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=choice(list[1])))
            elif type == 2:  # Ecoute
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=choice(list[2])))
            else:
                await client.change_presence(activity=discord.Streaming(name=choice(list[3]), url="https://www.twitch.tv/takaaase"))
            nbr_msg = 0
        else:
            nbr_msg += 1

    async def on_ready(self):
        """Fonction qui se lance au boot du bot."""

        # Montre que le bot est en ligne
        print('Logged in as')
        print(self.user.name)
        print('------')
        # await client.change_presence(activity=discord.Game(name="$$$what"))
        await client.change_presence(activity=discord.Streaming(name="$$$what", url="https://www.twitch.tv/takaaase"))

    async def on_message(self, message):
        """Fonction qui se lance à chaque message posté sur le serveur."""

        try:
            await self.set_status()
            # Evite que le bot ne se réponde à lui-même
            if message.author.id == self.user.id:
                return
            # On split le message des utilisateurs pour récupérer le premier mot.
            else:
                command_id = message.content.split(" ", 1)

            prefixe = str(await create_files(message))  # Récupération du préfixe du serveur

            if command_id[0] == "$$$what":  # Commande permettant de voir le préfixe du serveur
                await prefixe_show(prefixe, message)

            # Commande permettant de changer le préfixe du serveur
            if command_id[0] == prefixe + "prefixechange":
                await prefixe_change(prefixe, message)

            if command_id[0] == prefixe + "help":  # Commande Help
                await help_bot(prefixe, message)

            # ------ Commandes utiles ------

            if command_id[0] == prefixe + "poll":  # Commande sondage
                await poll_create(prefixe, message)

            # ------ Commandes jeux ------

            if command_id[0] == prefixe + "8ball":  # Commande boule magique
                await yes_no_ball(prefixe, message)

            if command_id[0] == prefixe + "russian":  # Commande roulette russe
                await russian(prefixe, message)

            # ------ Commandes administration ------

            if command_id[0] == prefixe + "clear":  # Commande Clear ADMIN ONLY
                await clear(prefixe, message)

            # ------ Commandes niveau et profils des utilisateurs ------

            if command_id[0] == prefixe + "profile":  # Commande profil
                await profil(prefixe, message)

            if command_id[0] == prefixe + "rank":  # Commande classement des utilisateurs
                await rank(prefixe, message)

            if command_id[0] == prefixe + "alert":  # Commande pour désactiver les messages d'alerte ADMIN ONLY
                await set_toogle_alert(message)

            # ------ Commandes anniversaire ------

            if command_id[0] == prefixe + "addbirth":  # Ajouter un anniversaire aux données du serveur
                await add_birth(prefixe, message)

            if command_id[0] == prefixe + "removebirth":  # Retirer un anniversaire des donnéesdu serveur
                await remove_birth(prefixe, message)

            if command_id[0] == prefixe + "nextbirth":  # Voir le prochain anniversaire du serveur
                await next_birth(prefixe, message)

            if command_id[0] == "anniv":
                await is_birth_today()

        except Exception as e:  # Si il y a une erreur dans les commandes, l'erreur est donnée sur discord directement.
            msg_embed = {
                "color": 15874618,  # Couleur de la barre
                "fields": [
                    # Zone 1
                    {
                        "name": "(╯°□°）╯︵ ┻━┻",
                        "value": f"""{e}"""
                    }],
                "footer":
                    {
                    "icon_url": "https://cdn.discordapp.com/attachments/487002983557627936/715329727757549568/portrait2.jpg",
                    "text": "Bot by Takase"
                },
                "title": "Error Bot"
            }
            await message.channel.send(embed=discord.Embed.from_dict(msg_embed))


client = MyClient()
client.run(TOKEN)
