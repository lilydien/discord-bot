from flask import Flask
from threading import Thread
import os
import discord
from discord.ext import commands

app = Flask("")
@app.route("/")
def home():
    return "✅ Bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

keep_alive()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 {bot.user} đã online")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

token = os.getenv("TOKEN")
if not token:
    raise SystemExit("TOKEN không được cấu hình. Thêm biến môi trường TOKEN khi deploy.")
bot.run(token)
