import os
import discord
from discord.ext import commands
from reporter import StreamGuard

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)
guard = StreamGuard("hkjnj018@gmail.com", "Saqer444$")

@bot.event
async def on_ready():
    print(f'البوت {bot.user} متصل وجاهز!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def start(ctx, url: str):
    await ctx.send(f"جاري بدء المراقبة لـ {url}...")
    result = guard.process(url)
    await ctx.send(f"النتيجة: {result}")

@bot.command()
async def no_dangerous(ctx, url: str):
    guard.safe_list.append(url)
    await ctx.send("تمت إضافة البث لقائمة التجاهل.")

bot.run(os.environ['DISCORD_TOKEN'])
