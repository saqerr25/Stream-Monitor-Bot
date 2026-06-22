import os
import discord
from discord.ext import commands
from reporter import perform_report

TOKEN = os.environ.get('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'البوت {bot.user} جاهز للعمل!')

@bot.command()
async def report(ctx, url: str, reason: str):
    await ctx.send(f"تم استلام طلبك للبلاغ عن: {url}")
    perform_report(url, reason)
    await ctx.send("تمت العملية بنجاح!")

bot.run(TOKEN)
