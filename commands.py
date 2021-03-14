import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil
from os import system
import random
from bot import gladge

@gladge.command(pass_context=True, aliases=['help'])
async def helpP(ctx):
    helpc = [
        ["hug {@user}","hug someone"]   
    ]
    embHelp = discord.Embed(title="How to use me", description="={command}", color=0xB7FF8B)
    for i in range(len(helpc)):
        embHelp.add_field(name=helpc[i][0], value=helpc[i][1], inline=False)
    await ctx.channel.send(embed=embHelp)