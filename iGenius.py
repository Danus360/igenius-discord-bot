import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time
import os
ban = ["436363464567"]

Client = discord.Client()
client = commands.Bot(command_prefix = "ig!")

@client.event
async def on_ready():
    print("Discord Version: " + discord.__version__)
    print(client.user.name + " is ready and serving Discord.")
    print("Client ID:" + client.user.name)
    await client.change_presence(game=discord.Game(name='ig!help | BETA'))    



@client.event
async def on_message(message):

    if message.content.lower().startswith("ig!cookie"):
        emb=discord.Embed(description=":cookie: ", color=0xd13bff)
        await client.send_message(message.channel, embed=emb)

    if message.content.lower().startswith("ig!readzattext"):
        f = open('Texts/Info.txt', 'r')
        content = f.read()
        emb=discord.Embed(description=content, color=0xd13bff)
        await client.send_message(message.channel, embed=emb)

    if message.content.lower().startswith("ig!suggest"):
        if message.author.id != ban:
            args = message.content.split(" ")
            msggg = "%s" % (" ".join(args[1:]))
            s = open('Texts/Suggestions.txt', 'a')
            s.write("\n" + message.author.name + "(" + message.author.id + ") - " + msggg)
            emb=discord.Embed(title="Message has been sent!", color=0xd13bff)
            await client.send_message(message.channel, embed=emb)
        else:
            emb=discord.Embed(description="You have been blocked from sending suggestions! And a report has been sent to Discord.. :( ", color=0xd13bff)
            await client.send_message(message.channel, embed=emb)


    if message.content.lower().startswith("dn!qwerty"):
        if message.author.id == "264806304609075200":
            args = message.content.split(" ")
            mesege = "%s" % (" ".join(args[2:]))
            await client.send_message(client.get_channel((args[1])), mesege)
        else:
            e = open('Texts/ErrorLog.txt', 'a')
            e.write("\n" + message.author.name + "(" + message.author.id + ") : Has used the GetChannel Message Command")
            emb=discord.Embed(description="Error: Permission Not Granted", color=0xd13bff)
            print(message.author.name + "(" + message.author.id + ") : Has used the GetChannel Message Command")
            await client.send_message(message.channel, embed=emb)


    if message.content.lower().startswith("ig!ping"):
        emb=discord.Embed(description='Pong!', color=0xd13bff)
        await client.send_message(message.channel, embed=emb)

    if message.content.lower().startswith('ig!say'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
   
    if message.content.lower().startswith("ig!flip"):
        cn=['Heads', 'Tails']
        emb=discord.Embed(description=random.choice(cn), color=0xffca38)
        await client.send_message(message.channel, embed=emb)

    if message.content.lower().startswith("ig!dice"):
        nmbrs= ['1','2','3','4','5','6']
        emb=discord.Embed(description=random.choice(nmbrs), color=0xffca38)
        await client.send_message(message.channel, embed=emb)   

    if message.content.lower().startswith("ig!8ball"):
        bl=["It is certain :8ball:","It is decidedly so :8ball:", "Without a doubt :8ball:","Yes, definitely :8ball:","You may rely on it :8ball:","As I see it, yes :8ball:","Most likely :8ball:",
            "Outlook good :8ball:","Yes :8ball:","Signs point to yes :8ball:","Reply hazy try again :8ball:","Ask again later :8ball:","Better not tell you now :8ball:","Cannot predict now :8ball:",
            "Concentrate and ask again :8ball:","Don't count on it :8ball:","My reply is no :8ball:","My sources say no :8ball:","Outlook not so good :8ball:","Very doubtful :8ball:"]
        emb=discord.Embed(description=random.choice(bl), color=0xffca38)
        await client.send_message(message.channel, embed=emb)

    if message.content.lower().startswith("ig!invite"):
        link = "Here is my invite :point_right:  :link:  https://discordapp.com/api/oauth2/authorize?client_id=412223157395652608&permissions=8&scope=bot"
        emb=discord.Embed(title="iGenius Invitation", description=link, color=0x3bf2ff)
        await client.send_message(message.author, embed=emb)

    if message.content.lower().startswith("ig!help"):
        hlp=discord.Embed(title="iGenius Commands List", description="\n \n \n Prefix: ig! \n \n Commands: \n \n Ping: Replies with Pong to demonstrate ping time \n Invite: Invitation Link so you can invite me to your server! :)  \n Cookie: Cookie emoji \n Flip: Random pick of either Heads or Tails \n Dice: Outputs a number 1-6 ", color=0x3b2ff)
        await client.send_message(message.author, embed=hlp)

    

client.run(procces.env.Token)
