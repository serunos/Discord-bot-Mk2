import os
from keep_alive import keep_alive
from discord.ext import commands
from replit import db
from random import randrange

bot = commands.Bot(
	command_prefix="$",  
	case_insensitive=True 
)

async def check_money(joueur,mise, ctx):
  
  if joueur in db.keys():  #trouve la thune du joueur dans la  db
    thune = int(db[joueur])
  else :
    await ctx.send("Vous n'avez jamais jouer, voici 1K pour bien démarrer")
    await ctx.send("Pour jouer veuillez recommencer")
    db[joueur]="1000"
    return

  if mise<=0 :
    await ctx.send("Vous devez miser plus que 0")
    return

  elif mise>argent :
    await ctx.send("Votre mise doit rentrer dans votre budget")
    return

  reste=argent-mise
  db[joueur]=reste

  return

@bot.event 
async def on_ready():  
  print(bot.user)  

@bot.command()
async def peroquet(ctx, arg):
  await ctx.send(arg)

@bot.command()
async def test(ctx, arg1, arg2):
  await ctx.send(ctx.author)

@bot.command()
async def roulette(ctx, nombre, mise):
  
  await ctx.send("la roulette n'est pas encore prête")
  print(nombre, mise)

  mise=int(mise)
  joueur=ctx.author

  await check_money(joueur,mise,ctx)
  

keep_alive()  
token = os.environ['token']
bot.run(token)  