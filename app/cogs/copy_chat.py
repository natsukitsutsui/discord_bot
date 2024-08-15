import os

import discord
from openai import OpenAI
from dotenv import load_dotenv
from discord.ext import commands

from utils.validate_reply import validate_reply

class CopyChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.collect_message()

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if validate_reply(ctx, self.bot, "CHAT_CHANNEL_ID"):
            return 
        
        openai_client = OpenAI(api_key=os.getenv("SECRET_KEY"))

        prompt = create_prompt()

        messages = [
            {"role": "system", "content": prompt},
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

    async def collect_message(self):
        # 既にファイルがあるならやらなくていいかも
        # updateコマンドを入れておくとか
        channel = self.bot.get_channel(int(os.getenv("COPY_CHANNEL_ID")))
        messages = []
        async for message in channel.history(limit=1000):
            if message.author.id == int(os.getenv("COPY_USER_ID")):
                messages.append(message.content)
        
        with open("data/user_message.txt", "w", encoding="utf-8") as f:
            for message in messages:
                f.write(f"{message}\n")
        
        print("Messages collected and saved to user_messages.txt")


def create_prompt():
    prompt = """
    以下の発言はあるユーザの発言履歴です。@はユーザメンションを表しています。あなたが発言する際はこのユーザのような話し方をして下さい。
    しかし、発言の仕方を真似るだけで過去の発言をそのまま引用することは絶対にしないでください。
    """
    with open("data/user_message.txt", "r", encoding="utf-8") as f:
        messages = f.readlines()
        for message in messages:
            prompt += f"{message}\n"
    return prompt

async def setup(bot):
    await bot.add_cog(CopyChatCog(bot))