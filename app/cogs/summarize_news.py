import discord
from openai import OpenAI
from discord.ext import commands

class SummarizeNewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="news")
    def summarize_news(self, ctx):
        if ctx.author == self.bot.user:
            return

        if ctx.channel.id != int(os.getenv("COMMANDS_CHANNEL_ID")):
            return