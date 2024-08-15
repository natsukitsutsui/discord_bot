import os
from dotenv import load_dotenv

load_dotenv()

def validate_reply(ctx, bot, channel):
    if ctx.author == bot.user:
        return True

    if ctx.channel.id != int(os.getenv(channel)):
        return True
    
    return False
    