import os
from keep_alive import keep_alive
from discord.ext import commands
from replit import db

keep_alive()  
token = os.environ.get("token") 

bot = commands.Bot(
	command_prefix="!",  
	case_insensitive=True 
)

async def check_argent(joueur):
  return

@bot.event 
async def on_ready():  
    print(bot.user)  


@bot.command
async def peroquet(ctx, arg):
  await ctx.send(arg)

@bot.command
async def test(ctx, arg, message):
  print(arg, message)

@bot.command
async def roulette(ctx, arg,message):
  return

bot.run(token)  