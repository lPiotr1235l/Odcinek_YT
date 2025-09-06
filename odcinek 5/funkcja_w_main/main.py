import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Zalogowano jako: [{bot.user.name}]')

# ---------------------

async def witaj_message(ctx):
    await ctx.channel.send("witaj")

# ---------------------

@bot.command()
async def witaj(ctx):
    await witaj_message(ctx)

# ---------------------
bot.run("TOKEN_BOTA")