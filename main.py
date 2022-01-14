import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def test(ctx, arg):
  await ctx.send(arg)

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("token") 
bot.run(token)  # Starts the bot