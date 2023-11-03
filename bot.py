import discord
from discord.ext import commands
from Token import token

bot = commands.Bot(command_prefix='>', self_bot=True)

@bot.event
async def on_ready():
	print(f'Logged on as {bot.user}!')
	print("Бот готов!")
	await bot.change_presence(status=discord.Status.online, activity=discord.Game("в очке пальцами"))

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)

bot.run(token)
#some commit