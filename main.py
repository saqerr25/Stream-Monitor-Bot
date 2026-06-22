import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'البوت {bot.user} متصل وجاهز!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def warn(ctx, url: str, *, msg: str):
    await ctx.send(f"جاري إرسال التحذير إلى {url}...")
    send_warning_to_stream(url, msg)
    await ctx.send("تمت العملية!")

def send_warning_to_stream(url: str, msg: str):
    """Send a warning to the specified stream"""
    pass

bot.run(os.environ['DISCORD_TOKEN'])
