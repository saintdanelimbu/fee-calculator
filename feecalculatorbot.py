import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
import random
from random import randint

#^ basic imports for other features of discord.py and python ^

client = discord.Client()
client = commands.Bot(command_prefix = '-',case_insensitive=True) #put your own prefix here
@client.event
async def on_ready():
    channel = client.get_channel(903690747197390888)
    await channel.send('DNA Fee Calculator is UP!')
    print("online")
client.remove_command('help')
##HANDLER CALCULATOR##   
@client.command()
async def goat(ctx,retail,selling):
    
    goatfee=float(selling) * 0.095 
    amountmade = float(selling) - float(goatfee)   
    cashoutfee= amountmade *0.029
    cashout = float(amountmade) - float(cashoutfee)
    profit = float(selling) - float(retail)
    sellingfee=[15,float(profit)*0.10]
    payout= float(selling) - float(goatfee) - float(cashoutfee) - float(max(sellingfee))
    
    embed = discord.Embed(
      description=f"""
      **RETAIL PRICE:** ${retail}
      **SELLING PRICE:** ${selling}
      **AMOUNT MADE (9.5%):** ${round(amountmade,2)}
      **CASHOUT FEE (2.9%):** ${round(cashout,2)}
      **SELLING FEE:** ${max(sellingfee)}

      **TOTAL PAYOUT:** **__${round(payout,2)}__**
      """,
      colour = discord.Colour.teal()
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_author(name='DNA GOAT FEE CALCULATOR')
    await ctx.send(embed=embed) 

##FEE CALCULATOR##   
@client.command()
async def fee(ctx,retail,selling):     
    profit = float(selling) - float(retail)
    sellingfee=[15,float(profit)*0.10]
    totalfees = max(sellingfee) + 10
    # payout= float(selling) - float(goatfee) - float(cashoutfee) - float(max(sellingfee))
    estimatedprofit = float(selling) -float(retail) -float(totalfees)
    estimatedpayout = float(estimatedprofit) + float(retail)
    
    embed = discord.Embed(
      description=f"""
      **SELLING PRICE:** ${retail}
      **RETAIL PRICE:** ${selling}
      **SERVICE FEE:** $10 / ₱500
      **SELLING FEE:** ${max(sellingfee)}
      ====================
      **TOTAL FEES:** **__${totalfees}__**
      ====================
      **ESTIMATED PAYOUT:** **__${round(estimatedpayout,2)}__**
      """,
      colour = discord.Colour.teal()
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_author(name='DNA FEE CALCULATOR')
    await ctx.send(embed=embed)

client.run("TOKEN")