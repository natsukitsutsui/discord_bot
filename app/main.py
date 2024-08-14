import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def setup_hook():
    await bot.load_extension("cogs.login")
    await bot.load_extension("cogs.example")
    await bot.load_extension("cogs.copy_chat")
    # await bot.load_extension("cogs.openai_chat")


bot.run(os.getenv("DISCORD_BOT_TOKEN"))