import discord
from discord.ext import commands
import funkcje
import config

bot = commands.Bot(command_prefix=config.PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Zalogowano jako: [{bot.user.name}]')

# ---------------------

@bot.command()
async def witaj(ctx):
    await funkcje.witaj(ctx)

# ---------------------
bot.run("TOKEN_BOTA")