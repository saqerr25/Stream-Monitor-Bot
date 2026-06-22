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
# أضف هذا الأمر في main.py
@bot.command()
async def warn(ctx, *, message: str = "تنبيه: محتوى مخالف، يرجى التوقف فوراً!"):
    # نقوم بإرسال الرسالة إلى البوت (الموجود في كلاس المراقبة)
    if hasattr(bot, 'current_driver'):
        try:
            chat_box = bot.current_driver.find_element(By.CSS_SELECTOR, "div#input")
            chat_box.send_keys(message + Keys.ENTER)
            await ctx.send(f"✅ تم إرسال التحذير إلى اليوتيوب: {message}")
        except Exception as e:
            await ctx.send(f"❌ فشل إرسال التحذير. تأكد من أن البوت يعمل: {e}")
    else:
        await ctx.send("❌ البوت غير متصل بأي بث حالياً. استخدم !start أولاً.")
        
