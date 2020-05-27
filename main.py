# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase
# Fichier principal

import discord
import asyncio
from param import *
from help import *

TOKEN = 'NzE0OTY0NTg4OTc3OTc5NDgz.Xs6u4Q.lImKoJDblVMIsHdavuEz30cFXbM'

class MyClient(discord.Client):
    async def on_ready(self):
        """Fonction qui se lance au boot du bot."""
        #Montre que le bot est en ligne
        print('Logged in as')
        print(self.user.name)
        print('------')
        #Statut du bot
        await client.change_presence(status=discord.Status.idle,
                                    activity=discord.Game("type $$$what"))

    async def on_message(self, message):
        """Fonction qui se lance à chauqe message posté sur le serveur."""

        #Evite que le bot ne se réponde à lui-même
        if message.author.id == self.user.id:
            return
        #On split le message des utilisateurs pour récupérer le premier mot.
        else :
            command_id = message.content.split(" ", 1)

        prefixe = str(await prefixe_file(message)) #Récupération du préfixe du serveur

        if command_id[0] == "$$$what": #Commande permettant de voir le préfixe du serveur
            await prefixe_show(prefixe, message)

        if command_id[0] == prefixe + "prefixe_change": #Commande permettant de changer le préfixe du serveur
            await prefixe_change(prefixe, message)

        if command_id[0] == prefixe + "help": #Commande Help
            await help_bot(prefixe, message)


client = MyClient()
client.run(TOKEN)
