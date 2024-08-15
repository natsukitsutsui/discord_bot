import os

import discord
from openai import OpenAI
from dotenv import load_dotenv
from discord.ext import commands

from utils.validate_reply import validate_reply

class OpenAIChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if validate_reply(ctx, self.bot, "CHAT_CHANNEL_ID"):
            return
        
        openai_client = OpenAI(api_key=os.getenv("SECRET_KEY"))
        messages = [
            {"role": "user", "content": ctx.content}
        ]

        completion = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )

        response = completion.choices[0].message.content

        await ctx.channel.send(response)

async def setup(bot):
    await bot.add_cog(OpenAIChatCog(bot))