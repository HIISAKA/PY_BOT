import discord      
from discord.ext import commands

import logging
from dotenv import load_dotenv\

import os
import asyncio

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
    
    for filename in os.listdir('./functions'):
        if not filename.endswith(".py") or filename.startswith("_"):
            continue
        if filename.endswith('.py'):
            await bot.load_extension(f'functions.{filename[:-3]}')

async def main():
    await load_extensions()
    async with bot:
        
        await bot.start(DISCORD_TOKEN)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Interrupted by user, shutting down.")