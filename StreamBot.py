from asyncio.exceptions import LimitOverrunError
from datetime import timedelta
from time import sleep
import discord
import os
import datetime
from discord import message
from ConfigForConfig import configureJson

from discord.message import flatten_handlers
from StreamerStatus import Streamer
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord.ext.commands import has_permissions


# load env vars and streamer config
load_dotenv()
time = datetime.datetime.now
configureJson()
cyd = Streamer("config.json")
cyd.getAccessToken()


# Create instance of client
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

async def announce():
    await bot.wait_until_ready()
    channel = bot.get_channel(807057710222147635)
    alreadyLive = 'no'
    while True:
        status = cyd.isLive()
        if status == "live" and alreadyLive =='no':
            await channel.send("Cyd is now LIVE on Twitch :partying_face:\n https://www.twitch.tv/originalcyd")
            alreadyLive = 'yes'
        if status != 'live' and alreadyLive == 'yes':
            alreadyLive = 'no'
        else: 
            pass

        await asyncio.sleep(1800)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$status'):
        await message.channel.send('StreamBot is Online.')
        
            


bot.loop.create_task(announce())
streamBotToken = os.environ.get('STREAMBOT_TOKEN')
bot.run(streamBotToken)
