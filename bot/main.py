import discord
from discord.ext import commands
from mcstatus import JavaServer
from mcstatus import BedrockServer


intents = discord.Intents.default()

bot = commands.Bot(command_prefix='?', intents=intents)

TOKEN = ""

@bot.event
async def on_ready():
    print('ready')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="Minecraft Servers"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandInvokeError):
        await ctx.reply("No such server was found")

@bot.command()
async def java(ctx, message):
    server = JavaServer.lookup(message)
    status = server.status()
    embed = discord.Embed(title=f"{message}", description=f"info on {message}")
    embed.add_field(name="Players Online :green_circle:", value=f"The server has {status.players.online} players online", inline=False)
    embed.add_field(name="Server Response :warning:", value=f"The server replied in {status.latency}ms", inline=False)
    await ctx.reply(embed=embed)

@bot.command()
async def bedrock(ctx, message):
    server = BedrockServer.lookup("message")
    status = server.status()
    embed = discord.Embed(title=f"{message}", description=f"info on {message}")
    embed.add_field(name="Players Online :green_circle:", value=f"The server has {status.players.online} players online", inline=False)
    embed.add_field(name="Server Response :warning:", value=f"The server replied in {status.latency}ms", inline=False)
    await ctx.reply(embed=embed)


bot.run(TOKEN)
