import discord
from openai import OpenAI
from discord.ext import commands

from utils.validate_reply import validate_reply

class SummarizeNewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="news")
    async def summarize_news(self, ctx):
        if validate_reply(ctx, self.bot, "COMMANDS_CHANNEL_ID"):
            return 
        
        await ctx.channel.send("Hello")


async def setup(bot):
    await bot.add_cog(SummarizeNewsCog(bot))
