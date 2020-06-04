import os
from google import GoogleApi
from db import DataBase
import discord
from dotenv import load_dotenv
from discord.ext import commands


#Create an object of Database
dbOb=DataBase("test.db")

#Load Token from .env file  
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Create a bot object
bot = commands.Bot(command_prefix='!')

#event when bot gets connected to discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

#event when new member joins the application
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )    

#event when messages arrives :Implemented reply to "hi" message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hi':
        await message.channel.send("hey")
    await bot.process_commands(message)

#handling command google : call Google Search Api
@bot.command(name='google')
async def googleApi(ctx,*,args):
    obj=GoogleApi()
    response=obj.callApi(args)
    dbOb.insertDb(str(ctx.author),args.lower())
    await ctx.send(response)

#handling command recent : return past history 
@bot.command(name='recent')
async def historyCheck(ctx,*,args): 
    response=dbOb.queryDb(str(ctx.author),args.lower())
    await ctx.send(response)

#run the bot
bot.run(TOKEN)