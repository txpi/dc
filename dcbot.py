from discord.ext.commands import Bot
from discord.ext import commands
from time import sleep
import platform
import discord
import asyncio
import random
import time
import os

#prefix
Client = discord.Client()
client = commands.Bot(command_prefix = "!")

#online
@client.event
async def on_ready():
    print("online.")
    
#commands
@client.event
async def on_message(message):
    
    if message.content.upper().startswith('!BANGER'):
        userID = message.author.id
        channel = client.get_channel("430339205172953118")
        bangers = ["https://soundcloud.com/user-138758645/jannitava-yokerho", "https://soundcloud.com/vtkmr/juppedog-potterin-luuta-family-friendly-version-prod-vtkmr", "https://soundcloud.com/user-807443016/ei-oo-homoo-diggaa-diqqi-tytyist?", "https://soundcloud.com/user-689702412/story-of-vidwaxgidy", "https://soundcloud.com/user-138758645/20-coronaa", "https://soundcloud.com/nuoripressa/og-odens-pre-a"]
        await asyncio.sleep(3)
        await client.send_message(channel, random.choice(bangers))

    if message.content.upper().startswith('!CHILL'):
        userID = message.author.id
        channel = client.get_channel("430339205172953118")
        sads = ["https://www.youtube.com/watch?v=2ie9Dejq5-4", "https://www.youtube.com/watch?v=FSuxh4a1QbY", "https://www.youtube.com/watch?v=Tu2TnagcIVc", "https://www.youtube.com/watch?v=poM9ac9JOU8", "https://www.youtube.com/watch?v=PSJAkItE7PQ"]
        await asyncio.sleep(3)
        await client.send_message(channel, random.choice(sads))
        
    if message.content.upper().startswith('!STEAM'):
        userID = message.author.id
        await client.send_message(message.channel, "http://steamcommunity.com/id/txpi/")

    if message.content.upper().startswith('!GROUP'):
        userID = message.author.id
        await client.send_message(message.channel, "```idk```")
        
    if message.content.upper().startswith('!BC'):
        userID = message.author.id
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % ("``` ```".join(args[1:])))
        await asyncio.sleep(0.1)
        await client.delete_message(message)

    if message.content.upper().startswith('!HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "```!banger - receive random track```")
        await client.send_message(message.channel, "```!chill - receive random track```")

    if message.content.upper().startswith('!NIGGER'):
        userID = message.author.id
        channel = client.get_channel("430339205172953118")
        blacks  = ["https://coubsecure-s.akamaihd.net/get/b93/p/coub/simple/cw_timeline_pic/0c2517ab5b8/bdec6724de3d56eb0e162/big_1471905246_image.jpg", "https://pbs.twimg.com/profile_images/697226438869704704/jRl8gGIg_400x400.jpg", "http://chimpmania.com/forum/attachment.php?attachmentid=61578&d=1400527619&thumb=1", "https://imagesvc.timeincapp.com/v3/mm/image?url=https%3A%2F%2Fpeopledotcom.files.wordpress.com%2F2016%2F08%2Flil-wayne-300-1.jpg%3Fw%3D300&w=700&q=85"]
        await asyncio.sleep(3)
        await client.send_message(channel, random.choice(blacks))
        
client.run("NDIwNjc1NDE0MjEwMzc5Nzc2.DYCIWw.US1G1MmzShXAA35QJFHhQM8gyyY")
