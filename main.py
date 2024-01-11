import discord
from discord import Game
import datetime
import time
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix='>', intents = discord.Intents.all())

membros_recebidos = []

@client.event
async def on_ready():
    print("Logged  in")
    print(client.user.name)
    print(client.user.id)
    print("-------------")

@client.event
async def on_member_join(member):
    guild = member.guild 

    if guild.id == "YOUR GUILD ID":     #   <=== https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID 
        channel_id = "YOUR CHANNEL ID"  #   <=== Make sure you get the ID of your channel by right-clicking it and clicking `Copy ID`. Make sure developer mode is on!
    elif guild.id == "YOUR GUILD ID":
        channel_id = "YOUR CHANNEL ID"
    elif guild.id == "YOUR GUILD ID":
        channel_id = "YOUR CHANNEL ID"
    channel = client.get_channel(channel_id)

    if channel is not None:
        embed = discord.Embed(title=f"YOUR MESSAGE, {member.name}!", description="YOUR MESSAGE!", color=0x9207ea)   #   <=== CHANGE IT TO YOUR PREFERRED COLOR and Change "YOUR MESSAGE" to the message of your choice
        embed.set_image(url="https://media.giphy.com/media/l0MYLYA2PediQmU6s/giphy.gif")
        await channel.send(embed=embed)
        membros_recebidos.append(member.id)


@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Olá Amigo :smile:")

client.run('YOUR TOKEN BOT')