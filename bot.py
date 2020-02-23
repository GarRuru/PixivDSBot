import discord
from discord.ext import commands
import json
import requests
import os

bot = commands.Bot(command_prefix='k!')
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


@bot.event
async def on_ready():
    print(">>Bot is online!")

@bot.event
async def on_member_join(member):
    print(f"{member} join")
    channel = bot.get_channel(678507023935209474)
    await channel.send(f"{member} join")


@bot.event 
async def on_member_remove(member):
    print(f"{member} leave")
    channel = bot.get_channel(678507023935209474)
    await channel.send(f"{member} leave")
 
@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000} ms')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension} complete.')






if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
