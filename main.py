import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents) # sets the prefix 

# what happens when bot starts
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!cmds')) # give it a status
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})') # Prints the bots username and the ID

# command template
@bot.command()
async def cmds(ctx):
    embed = discord.Embed(title="List of available commands:",) # description="",) #color=808080) 
    embed.add_field(name="!cmds", value="Displays this help message.", inline=False)
    await ctx.send(embed=embed)

# run the bot
bot.run('YOUR-DISCORD-BOT-TOKEN')
