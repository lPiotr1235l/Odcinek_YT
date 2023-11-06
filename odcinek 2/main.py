import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Zalogowano jako: [{bot.user.name}]')

# ---------------------

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.command()
async def embed(ctx):
    embed = discord.Embed(description="embeda stworzona na potrzeby odcinka", colour=0xf3128a)
    embed.set_author(name="Programowanie Python", icon_url="https://icon-library.com/images/code-icon-png/code-icon-png-0.jpg")
    embed.set_thumbnail(url="https://cdn.expose.pl/wp-content/uploads/2022/02/code-g5cbc31789_1920.jpg")
    await ctx.send(embed=embed)

# ---------------------
bot.run("Token Bota")