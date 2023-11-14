import discord
from discord.ext import commands

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

@bot.command()
async def reset(ctx):
    await ctx.send("reset statusu")
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def graj(ctx):
    await ctx.send("Zmieniono status na Graj")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name='Minecraft'))

@bot.command()
async def sluchaj(ctx):
    await ctx.send("Zmieniono status na Słuchaj")
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name='Muzyki'))

@bot.command()
async def ogladaj(ctx):
    await ctx.send("Zmieniono status na Oglądaj")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='Youtube'))

@bot.command()
async def rywalizuj(ctx):
    await ctx.send("Zmieniono status na Rywalizuj")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.competing, name='Konkursie'))

@bot.command()
async def custom(ctx):
    await ctx.send("Zmieniono status na Custom")
    await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='😎 Idzie na długi spacer'))

@bot.command()
async def test(ctx, nazwa: str):
    await ctx.send("Zmieniono status na Test")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=f'{nazwa}'))

@bot.command()
async def clear(ctx, ilosc: int):
    await ctx.channel.purge(limit=ilosc + 1)

# ---------------------
bot.run("Token Bota")