#-------------------------------------------------------------
#                   Python StephanieBot
#-------------------------------------------------------------
#Auteurs:
#- Louka Placé -> à founit certaines commande du cobrabot
#- Olivier Palvadeau -> créateur du projet
#- Paul Coignac -> à founit certaines commande du cobrabot

#Version: 1.4

#Description Globale:
#Ce programme a été créé à partir d'un autre projet (CobraBot)
#Ce programme fonctionne avec l'API discord pour python
#Le programme envoi des informations de script python au bot
#Le bot garde le code en mémoire
#Ce code permet donc de coder notre Bot Discord (Stephanie)

#Description du Bot:
    #Permet globalement, de attribuer des roles aux nouveaux
    #arrivants
#Attention:
#Ce fichier doit être accompagné de quatre fichiers texte vides(sans \n ou espaces):
# - Servers.txt
# - ServersPrefix.txt
# - rulesChannel.txt
# - Roles.txt
#certaines informations sont à completer par vous-même
#-------------------------------------------------------------
#Importations de modules et packages:
#-------------------------------------------------------------
import discord
import asyncio
#-------------------------------------------------------------
#             Début du programme:
#-------------------------------------------------------------

bot = discord.Client() #l'objet bot correspond au Bot, il s'agit d'un client 
#id d'utilisateurs gérant le bot:
Own1 = (votre id) #id du gérant du bot / à compléter avec votre id sans les ()



    
    
#************************************************************************************************************************************************
#                                             Listes informations
#************************************************************************************************************************************************
def cleanList(liste):
    for index in range(len(liste)):                      #cette fonction permet d'effacer le \n pour chaque terme de la liste
        liste[index] = liste[index].replace("\n", "")
    return liste
def listType(liste, dataType):                           #cette fonction permet de changer le type de chaque terme de la liste
    if dataType == "int":
        for i in range(len(liste)):
            liste[i] = int(liste[i])
        return liste
    elif dataType == "str":
        for i in range(len(liste)):
            liste[i] = str(liste[i])
        return liste
S = open("Servers.txt","r")
Servers = S.readlines();                     #Liste qui contiendra les ID de serveurs
S.close()
Servers = cleanList(Servers)
Servers = listType(Servers, "int")           #la liste devient une liste d'entiers
print("Servers ID:", Servers)
SP = open("ServersPrefix.txt","r")
ServersPrefix = SP.readlines();              #liste qui contiendra les Prefixes de chaques serveurs
SP.close()                                   #il s'agit de la marque permettant au bot d'identifier qu'il s'agit du'une commande
ServersPrefix = cleanList(ServersPrefix) 
print("Prefixes:", ServersPrefix)
RC = open("rulesChannel.txt","r")
rulesChannel = RC.readlines();               #liste qui contiendra les différents salons
RC.close()
rulesChannel = cleanList(rulesChannel)
rulesChannel = listType(rulesChannel, "int") #la liste devient une liste d'entiers
print(rulesChannel)
R = open("Roles.txt", "r")
Roles = R.readlines();
R.close()
Roles = cleanList(Roles)
Roles = listType(Roles, "int")

#***************************************************************************************************************************************************


#************************************************************************************************************************************************
                                             #Connection au bot
#************************************************************************************************************************************************
@bot.event #Décorateur(la fonction ne peut pas fonctionner si il n'y a pas d'évenement)
async def on_ready():                               #Si le bot est prêt et connecté, la fonction est appelée
    print("Bot connecté:", bot.user.name)           #On affiche le nom du bot trouvé
    print("Bot id:", bot.user.id)                   #On affiche l'id du bot trouvé, si jamais il n'a pas un nom à jour
    botOwner1 = bot.get_user(Own1)       #crée un objet de type user avec l'id du user
    #envoi un message aux gérants du bot
    await botOwner1.send("Le bot vient de démarrer!"); 
    await botOwner1.send(f"Serveurs connectés: {Servers}"); 
#Fin de la connection au bot
#************************************************************************************************************************************************
    
    
#***************************************************************************************************************************************************
#                                                   Commandes dans le chat
#                                              et reconnaissance des serveurs
#***************************************************************************************************************************************************
@bot.event
async def on_message(message):          #La fonction est appelée si le bot lit un message dans le chat
    #On utilise les listes en global
    global ServersPrefix
    global Roles
    global Servers
    global rulesChannel
    global Serv
    if message.author == bot.user:      #Si l'auteur du message est le bot, ne fait rien.
        return
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #Reconnaissance du serveur:
    if message.content:                 #Si le bot détecte un message autre que le sien
        Serv = [message.guild.id];      #liste contenant l'id du serveur ou a été reçu le message
        ServPrefix = "";                #Variable de type string qui contiendra un préfix temporaire
        
        #Si le serveur n'est pas dans la base de données(liste Serveurs):
        if Serv[0] not in Servers: 
            Servers = Servers + Serv                               #On concatène (on ajoute un terme dans la liste) (On rajoute une Id de serveur)
            ServPrefix = "!";                                      #Le préfixe temporaire prend cette valeur
            ServersPrefix = ServersPrefix + list(ServPrefix)       #On concatène (on ajoute un terme dans la liste) (on rajoute un préfixe dans la liste)
            ServRulesChannel="0";                                  #On définit un salon 0 si le serveur n'est pas dans la base de donnée
            ServRole = [0];
            rulesChannel=rulesChannel + list(ServRulesChannel)
            Roles = Roles + ServRole
        
        #Sinon (si le serveur est dans la base de données(liste Serveurs):
        else: 
            for s in range(0,len(Servers)):
                if Servers[s] == Serv[0]:
                    ServPrefix = ServersPrefix[s]        #Le préfixe temporaire prend la valeur du préfixe du serveur correspondant
                    ServRulesChannel = rulesChannel[s]
        #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    
        #Commande test:
        #Le bot envoi un message test
        if message.content == f"{ServPrefix}test" or message.content == f"{ServPrefix}Test" or message.content == f"{ServPrefix}TEST":
            await message.channel.send(f"Bonjour à toi {message.author.mention}!! Je fonctionne très bien!")# le bot envoi un message dans le canal où il a lu la commande
        
        #Commande CobraBot:
        #Le bot explique ce pour quoi il a été créé
        if message.content == f"{ServPrefix}Stephanie" or message.content == f"{ServPrefix}stephanie" or message.content == f"{ServPrefix}STEPHANIE":
            await message.channel.send(f"Bonjour {message.author.mention} , je suis un robot qui a pour rôle de vous servir, c'est grâce à moi que les rôles sont atribués immédiatement aux arrivants")# le bot envoi un message dans le canal où il a lu la commande
        
        #Commande rules:
        if message.content == f"{ServPrefix}rules" :
            ServRulesChannel = message.channel.id            #récupère l'id du salon
            for s in range(0,len(Servers)):
                if Servers[s] == Serv[0]:
                    rulesChannel[s] = ServRulesChannel
            await message.channel.send("Ce salon est maintenant le salon règlement")

        #Commande prefix:
        #Le bot change le prefixe du serveur correspondant dans la base de données(liste ServersPrefix)
        if message.content.startswith(f"{ServPrefix}prefix"):
            newprefix = message.content;                   #On reprend le message entier de l'utilisateur
            #On enlève des éléments au message
            newprefix = newprefix.replace(f"{ServPrefix}prefix","")
            newprefix = newprefix.replace(" ", "")
            #il ne reste plus que le préfixe dans la variable
            for s in range(0,len(Servers)):
                if Servers[s] == Serv[0]:
                    ServersPrefix[s] = newprefix           #Le préfixe correspondant au serveur dans la base de donnée est remplacé par le nouveau
            await message.channel.send(f"Le prefix a été remplacé par '{newprefix}'")      # Le bot envoi un message
            #************************************************************************************
        
        #commande role:
        if message.content.startswith(f"{ServPrefix}role"):
            t=0 #marqueur 0 -> déjà un role, 1 -> pas de role
            for s in range(0,len(Servers)): #on cherche l'id du rôle en fonction du serveur
                if Servers[s] == Serv[0]:
                    roleId = Roles[s]
                    role = message.guild.get_role(roleId)
                if roleId == 0: #si l'id n'est pas encore définie
                    role = message.guild.default_role.id
                    t = 1
            #traitement du message:
            RoleName = message.content
            RoleName = RoleName.replace(f"{ServPrefix}role","")
            RoleName = RoleName.replace(" ", "")
            #message traité (il ne rest plus que le nom)
            
            if t == 1: #si il n'y a pas de rôle, on en crée un
                newrole = await message.guild.create_role(name = RoleName, permissions = discord.Permissions(0));
                for s in range(0,len(Servers)):
                    if Servers[s] == Serv[0]:
                        Roles[s] = newrole.id #Le rôle correspondant au serveur dans la base de donnée est remplacé par le nouveau
                await message.channel.send(f"J'ai créé un nouveau role d'arrivées intitulé '{RoleName}'")
            elif t == 0: #si il y a déjà un rôle, on modifie son nom
                lastn = role.name
                await role.edit(name = RoleName) #on renomme le rôle
                await message.channel.send(f"J'ai changé le nom du role d'arrivées intitulé '{lastn}' par '{RoleName}'")
                
        #Pour les test:
        print("servers:",Servers)           #affiche les serveurs dans la console
        print("Prefixes:",ServersPrefix)    #affiche le prefix des serveurs dans la console
        print ("Rules Channel:",rulesChannel)
        print("Roles:", Roles)
        
        #écriture dans les fichiers:
        S = open("Servers.txt", "w")
        for ligne in Servers:
            S.write(str(ligne)+"\n")
        S.close()
        SP = open("ServersPrefix.txt", "w")
        for ligne in ServersPrefix:
            SP.write(str(ligne)+"\n")
        SP.close()
        RC = open("rulesChannel.txt", "w")
        for ligne in rulesChannel:
            RC.write(str(ligne)+"\n")
        RC.close()
        R = open("Roles.txt", "w")
        for ligne in Roles:
            R.write(str(ligne)+"\n")
        R.close()
        
        

    
        
#await nous permet d'appeler la fonction de l'API discord étant donné que nous sommes dans une fonction async
#Fin messages
   
#************************************************************************************************************************************************

#************************************************************************************************************************************************
#                                             Lorsque un membre rejoint le serveur
#************************************************************************************************************************************************
@bot.event
async def on_member_join(member):          #La fonction est appelée si quelqu'un rejoint le serveur
    global Roles
    Serv = [member.guild.id]
    for s in range(0,len(Servers)):
        if Servers[s] == Serv[0]:
            roleId = Roles[s]                 
            if roleId == 0:
                roleId = member.guild.default_role.id
                role = member.guild.default_role
            else:
                role = member.guild.get_role(roleId)
                
    await member.add_roles(role)
        
    await member.send("Bonjour à toi " + member.mention + " et bienvenu sur le serveur " + member.guild.name ) #Envoie un message de bienvenue au membre qui rejoint
    for s in range(0,len(Servers)):
        if Servers[s] == Serv[0]:
            channelId = rulesChannel[s]                 #On récupère le salon de règle correspondant au serveur -> temporairement
            channel = bot.get_channel(channelId)        #on crée un objet du type channel avec l'id du salon
    if channelId != 0:                                  #0 signifie qu'il n'y a pas de salon règle définit
        await member.send(f"Veuillez lire le salon {channel.mention}.")
    R = open("Roles.txt", "w")
    for ligne in Roles:
        R.write(str(ligne)+"\n")
    R.close()
#*************************************************************************************************************************************************

#*************************************************************************************************************************************************
#                                                  Lorsque un membre quitte le serveur
#*************************************************************************************************************************************************
@bot.event
async def on_member_remove(member):                                              #La fonction est appelée si quelqu'un quitte le serveur
    await member.send("Reviens  quand tu veux " + member.mention + "sur" + member.guild.name )  #envoie du message dans le channel d'arrivée qui le System Channel
#*************************************************************************************************************************************************

#*************************************************************************************************************************************************
    #Lorsque une quelqu'un ajoute le bot à son serveur
#*************************************************************************************************************************************************

@bot.event
async def on_guild_join(guild):
    await guild.system_channel.send("Bonjour à vous! Merci d'avoir choisi le Bot Stephanie!!!")

#*************************************************************************************************************************************************




#Doit être utilisé en dernier
bot.run("votre token") #à complété avec votre token
#On met en ligne le bot à partir de son Token (dispo sur le site développeur de discord)