import discord
import time
from discord.ext import commands
import io
import aiohttp
from config import *


bot = commands.Bot(command_prefix='!') #sets the prefix





@bot.command()
async def test(ctx):
   await ctx.reply('hello')
@bot.command()
async def vore(ctx):
    await ctx.reply("*you nom your tail accidently*")



@bot.command()
async def cat(ctx):


    async with aiohttp.ClientSession() as session:
        async with session.get("https://cataas.com/cat") as resp:
         if resp.status != 200:
            return await ctx.send('error getting file') 
         data = io.BytesIO(await resp.read())
         await ctx.reply(file=discord.File(data, "cat.png" ))

@bot.command()

async def dog(ctx):


    async with aiohttp.ClientSession() as session:
        async with session.get("https://placedog.net/640/480?random") as resp:
         if resp.status != 200:
            return await ctx.send('error getting file')
         data = io.BytesIO(await resp.read())
         await ctx.reply(file=discord.File(data, "480.png" ))

bot.run(TOKEN) #this is set on the config.py file
