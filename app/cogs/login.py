import discord
from discord.ext import commands

class LoginCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name} - {self.bot.user.id}")
        print("------")
        for cog in self.bot.cogs:
            print(f'Loaded cog: {cog}')

async def setup(bot):
    await bot.add_cog(LoginCog(bot))