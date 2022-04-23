# StatusMC
This bot uses the [mcstatus](https://github.com/py-mine/mcstatus) library
### Startup
Create a `requirements.txt` file to install the required libraries to make the bot
```python
discord
mcstatus
```

Import the correct libraries
```python
import discord #allows the bot to use the discord api and discord.py library
from discord.ext import commands #enables the use of discord commands
from mcstatus import JavaServer #this allows the bot to query java servers
from mcstatus import BedrockServer #this allows the bot to query bedrock servers
```

Enable intents, [read more here](https://discordpy.readthedocs.io/en/latest/intents.html)
```python
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='?', intents=intents)

TOKEN = "YOUR_TOKEN_HERE" #replace YOUR_TOKEN_HERE with your discord bot's token
```

Adding custom status
```python
@bot.event
async def on_ready():
    print('ready')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="Minecraft Servers"))
```

Error handling
```python
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandInvokeError):
        await ctx.reply("No such server was found")
```
Java command. Use: ?java example.org
```python
@bot.command()
async def java(ctx, message):
    server = JavaServer.lookup(message)
    status = server.status()
    embed = discord.Embed(title=f"{message}", description=f"info on {message}")
    embed.add_field(name="Players Online :green_circle:", value=f"The server has {status.players.online} players online", inline=False)
    embed.add_field(name="Server Response :warning:", value=f"The server replied in {status.latency}ms", inline=False)
    await ctx.reply(embed=embed)
```
Bedrock command. Use ?bedrock example.org:port
```python
@bot.command()
async def bedrock(ctx, message):
    server = BedrockServer.lookup("message")
    status = server.status()
    embed = discord.Embed(title=f"{message}", description=f"info on {message}")
    embed.add_field(name="Players Online :green_circle:", value=f"The server has {status.players.online} players online", inline=False)
    embed.add_field(name="Server Response :warning:", value=f"The server replied in {status.latency}ms", inline=False)
    await ctx.reply(embed=embed)
```

Run the bot
```python
bot.run(TOKEN)
```
