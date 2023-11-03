import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix="Wasz Prefix Bota", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Zalogowano jako: [{bot.user.name}]')

# ---------------------

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

# ---------------------
bot.run("Wasz Token Bota")