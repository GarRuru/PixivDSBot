import discord
from discord.ext import commands

class cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
