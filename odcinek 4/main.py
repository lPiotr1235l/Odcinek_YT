import discord
from discord.ext import commands
import config
import zmienne

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Zalogowano jako: [{bot.user.name}]')
    print(f'{zmienne.zmienna1}')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name=f'{zmienne.zmienna1}'))

# ---------------------

@bot.command()
async def test(ctx):
    zmienna2 = zmienne.zmienne_all["zmienna2"]
    zmienna3 = zmienne.zmienne_all["zmienna3"]
    
    await ctx.send(f"{zmienne.zmienna1}, {zmienna2}, {zmienna3}")

@bot.command()
async def clear(ctx, ilosc: int):
    await ctx.channel.purge(limit=ilosc + 1)

# ---------------------
bot.run("Token Bota")