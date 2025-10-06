import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Xin chào!")

bot.run(os.getenv("DISCORD_TOKEN"))
