import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil
from os import system
from dotenv import load_dotenv
import random
import string
import json
from prsaw import RandomStuff #inititate AI repository, Import module DO NOT MESS WITH,. License belongs to https://pypi.org/project/prsaw/

#initiate bank
os.chdir("bank")

#iniate token
load_dotenv()

#initiate prefix
PREFIX = '='
gladge = commands.Bot(command_prefix=PREFIX, help_command=None)
gladgeTalk = RandomStuff(async_mode = True)

#indication that Zhu Li started
@gladge.event
async def on_ready():
    print('Logging in as {0.user}'.format(gladge))
    await gladge.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name='type =gladge'))

# Testing functions/ Misc.
@gladge.event
async def on_message(message):
    if message.author == gladge.user:
        return
    
    if message.content.startswith("=who is your creator"):
        await message.reply("Ej is my creator")
    elif message.content.startswith("=who is your creator"):
        await message.reply("Ej is my creator")
    elif message.content.startswith("=I am your creator"):
        await message.reply("No, Ej is my creator")
    elif message.content.startswith("=i am your creator"):
        await message.reply("No, Ej is my creator")
    elif message.content.startswith("=whats your name"):
        await message.reply("Gladge bot")
    elif message.content.startswith("=what's your name"):
        await message.reply("Gladge bot")
    elif message.content.startswith("=what's your name?"):
        await message.reply("Gladge bot")
    elif message.content.startswith("=what is your name"):
        await message.reply("Gladge bot")
    elif message.content.startswith("=what is your name?"):
        await message.reply("Gladge bot")
    elif message.content.startswith("=who's ej's dj"):
        await message.reply("jeni is ej's dj")
    elif message.content.startswith("=who's jeni's dj"):
        await message.reply("ej")
    else:
        if message.content.startswith("="):
            response = await gladgeTalk.get_ai_response(message.content)
            await message.reply(response)

    await gladge.process_commands(message)    # allows that use of an event before command decorators

@gladge.command(pass_context=True, aliases=['help'])
async def helpP(ctx):
    helpc = [

        #["",""],  <-- format to add in help
        ["gladge","introduction"],
        ["hug {@user}","send them a hug emote"],
        ["violin","Mr.Krabs playing a sad song in the world's smallest violin. To play the sound, have gladge be in vc."],
        ["come","Gladge will join VC"],
        ["rocklet","Ari's favorite command"],
        ["hi", "Greet Gladge bot"],
        ["alexaQuote","A pick me up quote from the meme queen herself"],
        ["sadgeRain","for sad hours - One of Alex's personal gif commads"],
        ["teleRun","run! - One of Alex's personal gif commads"],
        ["momoChaos","momo being chaotic - One of Alex's personal gif commads"],
        ["jamesChaos","james being chaotic - One of Alex's personal gif commads"],
        ["identifyBird {picture attachment}","[currently in progress EST 2021]"],
        ["mugiStan","Proof that Alex is a mugi stan and not a Mio stan"],
        ["modApp","Mod application read by Alex"],
        ["endgame","Endgame archie quote read by Alex"],
        ["cout", "cout."]
    ]
    embHelp = discord.Embed(title="How to use me", description="={command}\n", color=0xB7FF8B)
    for i in range(len(helpc)):
        embHelp.add_field(name=helpc[i][0], value=helpc[i][1], inline=False)
    await ctx.channel.send(embed=embHelp)

@gladge.command(pass_context=True, aliases=['gladge'])
async def intro(ctx):
    embedMsg = discord.Embed(title="Hello! I'm Gladge, your personal bot made by a cout (Po), for couts", colour=discord.Colour(0xffafe3), description="I was materialized from pure chaotic energy in the flames of degen hours. These degens have put together their ideas to make Ej write a bot specifically for their needs. In typical fashion, they made a programmer work in grueling hours of unpaid work to write a bot just for a joke.")

    embedMsg.set_thumbnail(url="https://cdn.discordapp.com/avatars/211003392347209729/a_562bc1a36d487e3cec4cd56d60d53e84.gif")
    embedMsg.set_author(name="Gladge Bot", icon_url="https://cdn.discordapp.com/app-icons/815058864294068264/d3c6d351695533a8e3d344438f09c7d2.png")
    embedMsg.set_footer(text="Ej™", icon_url="https://cdn.discordapp.com/avatars/211003392347209729/a_562bc1a36d487e3cec4cd56d60d53e84.gif")

    embedMsg.add_field(name="Who are these couts that have percieved me", value="  -")
    embedMsg.add_field(name="Arioli Ravioli", value="aka Ari: https://www.twitch.tv/arioli", inline=False)
    embedMsg.add_field(name="Cout 2", value="aka Alexa: https://www.twitch.tv/wwhisper", inline=False)
    embedMsg.add_field(name="Mom/kararara", value="aka Alex: https://www.twitch.tv/kkalexandria", inline=False)
    embedMsg.add_field(name="Devoid", value="aka Devoid: https://www.twitch.tv/devoidxx", inline=False)
    embedMsg.add_field(name="MoMoo", value="aka momo: https://www.twitch.tv/momoobun", inline=False)
    embedMsg.add_field(name="----------------------------------------------------------------------", value="```To see my commands type =help```")

    await ctx.channel.send(embed=embedMsg)

@gladge.command(pass_context=True, aliases=['hi', 'hello', 'hi!', 'hello!', 'hoi', 'HI', 'Hi', 'Hello', 'Hi!', 'Hello!', 'hey', 'Hey'])
async def greetings(ctx):
    user = {ctx.author.name}
    if str(ctx.author) in ["alexa#4302"]:
            responses = ["HI QUEEN, OMG HOW ARE YOU GIRL!", "KAAA WEEEN, WURK IT!", "FLAWLESS, KAA WEEeeEEN!", "Hello cout 2!"]
            choice = random.choice(responses)
            await ctx.channel.send(choice)
    elif str(ctx.author) in ["parsecs#0001"]:
            await ctx.channel.send("Greetings, creator.")
    elif str(ctx.author) in ["ari 🌿#1166"]:
            await ctx.channel.send("<:pointLaugh:814011766785835008> Hello Arioli Ravioli!")
    else:
        responses = [f"Hello {ctx.author.name}.", f"Hi {ctx.author.name}.", f"Greetings, {ctx.author.name}.", f"Pleasure to see you, {ctx.author.name}.", f"Good day to you, {ctx.author.name}."]
        choice = random.choice(responses)
        await ctx.channel.send(choice)

@gladge.command(pass_context=True, aliases=['hug'])
async def hugs(ctx):
    user = ctx.author.mention
    await ctx.send("<:gibHug:814011919399649280>")

@gladge.command(pass_context=True, aliases=['violin'])
async def vio(ctx):
    await ctx.channel.send(file=discord.File('gifs/crabsViolin.gif'))

    channel = ctx.message.author.voice.channel #chennel author is in
    vcCheck = get(gladge.voice_clients, guild=ctx.guild)
    # vcCheck = ctx.member.voice

    # if vcCheck is None:
    #     await ctx.send('No one is in VC')
    # else:
    #     await ctx.send('you are in VC')

    def end():
        print ("completed the sound clip")

    playState = 1
    #if fladge is not in vc
    if vcCheck == None:
        await channel.connect()
        voice = get(gladge.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("soundbytes/violin.mp3"), after=lambda e: end())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.65


    #if gladge is in vc
    else:
        voice = get(gladge.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("soundbytes/violin.mp3"), after=lambda e: end())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.65


@gladge.command(pass_context=True, aliases=['come'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    vc = get(gladge.voice_clients, guild=ctx.guild)

    if vc and vc.is_connected():
        await vc.move_to(channel)
    else:
        vc = await channel.connect()

    if vc and vc.is_connected():
        await vc.move_to(channel)
    else:
        vc = await channel.connect()
        print(f"Gladge connected to {channel}\n")

    await ctx.send(f"Gladge has connected to {channel}")

@gladge.command(pass_context=True, aliases=['rocklet'])
async def rockletComms(ctx):
    await ctx.channel.send("imagine thinking rocklet wont last forever. like it isn't written in the stars. like they aren't my one true pairing. like they weren't programmed into the game purely to live on your island as a duo. i curse you with rocket and violet. may they move to your island and never have a thought bubble. may they force you to reset and somehow both become your starters for eternity. may you be trapped in the rocklet nation for life. -sattie")
    await ctx.channel.send(file=discord.File('pics/rocklet.png'))

@gladge.command(pass_context=True, aliases=['alexaQuote'])
async def alexabeglad(ctx):
    await ctx.channel.send("be gladge not sadge - alexa")

@gladge.command(pass_context=True, aliases=['sadgeRain'])
async def sadgeRainGif(ctx):
    await ctx.channel.send(file=discord.File('gifs/sadge.gif'))

@gladge.command(pass_context=True, aliases=['teleRun'])
async def teletubRuns(ctx):
    await ctx.channel.send(file=discord.File('gifs/telerun.gif'))

@gladge.command(pass_context=True, aliases=['momoChaos'])
async def momoChaotic(ctx):
    await ctx.channel.send(file=discord.File('gifs/momoBoom.gif'))

@gladge.command(pass_context=True, aliases=['jamesChaos'])
async def jamesChaotic(ctx):
    await ctx.channel.send(file=discord.File('gifs/jamesBoom.gif'))

@gladge.command(pass_context=True, aliases=['MugiStan', 'mugiStan', 'mugistan'])
async def mugimugi(ctx):
    def end():
        print ("completed the sound clip")
        return

    voice = get(gladge.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("soundbytes/mugistan.mp3"), after=lambda e: end())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.75

@gladge.command(pass_context=True, aliases=['modApp'])
async def couters(ctx):
    def end():
        print ("completed the sound clip")
        return

    voice = get(gladge.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("soundbytes/cout.mp3"), after=lambda e: end())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.20

@gladge.command(pass_context=True, aliases=['endgame'])
async def whyers(ctx):
    def end():
        print ("completed the sound clip")
        return

    voice = get(gladge.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("soundbytes/endgame.mp3"), after=lambda e: end())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.25

@gladge.command(pass_context=True, aliases=['cout'])
async def realcout(ctx):
    def end():
        print ("completed the sound clip")
        return

    voice = get(gladge.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("soundbytes/realcout.mp3"), after=lambda e: end())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.75

@gladge.command(pass_context=True, aliases=['t'])
async def talk(ctx):
    if gladge.user == ctx.author:
        return
    response = await gladgeTalk.get_ai_response(ctx.content)
    await ctx.reply(response)


gladge.run(os.getenv('TOKEN'))








# @gladge.command(pass_context=True, aliases=['bal'])
# async def balalnce(ctx):
#     await openAcc(ctx.author)


# async def openAcc(user):
#     with open("bank.json", "r") as f:
#         users = json.load(f)
#     if str(user.id) in users:
#         return False
#     else:
#         users[str(user.id)]["wallet"] = 0
#         users[str(user.id)]["bank"] = 0

#     with open("bank/bank.json", "w") as f:
#         json.dump(users, f)
#     return True

# async def get_bank_data():
#     with open("")