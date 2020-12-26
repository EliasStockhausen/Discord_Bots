# bot.py
import os
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

from sbahn import sbahn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('CleanBot')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='cleanup', help='Removes all unpinned messages')
async def clean(ctx):
    channel = ctx.channel
    messages = await channel.history(limit=500).flatten()
    for msg in messages:
        logger.info(f'Message: {msg.created_at} by {msg.author.name} is pinned  {msg.pinned}')

        if not msg.pinned:
            logger.info(f'Deleting Message')
            await msg.delete()

#departures = sbahn.departure_eching()
#
#for departure in departures:
#    departure.line       # line
#    departure.to         # direction
#    departure.at         # leaves at
#    departure.minutes    # leaves in ...
#    departure.is_delayed # True/False
#    departure.delay      # in minutes
#

bot.run(TOKEN)
