import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công dưới tên: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! Bot đang hoạt động!")

bot.run(os.getenv("TOKEN")) 
