# You Can (Not) Advance (You're (Not) Alone 2.0)
# Author : Takase

import discord
import asyncio

async def create_files(message):
    """Fonction chargée de créer les différents fichiers des serveurs"""

    id_serveur = message.guild.id #Récupération de l'ID du serveur

    try : #On regarde si les fichiers existent déjà pour le serveur
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt", "r") #Test Fichier Russian
        #Autres fichiers ici
        return

    except : #Si les fichiers n'existent pas
        try :  #On essaye de créer le dossier du serveur
            os.mkdir("./files/"+str(id_serveur))
        except :
            pass
        #Fichier Russian
        text_file = open("files\\"+str(id_serveur)+"\\russian.txt","w+")
        text_file.write("False\nFalse\nFalse\nFalse\nFalse\nTrue")
        #Autre fichiers ici
        return
