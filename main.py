import discord
from discord.ext import commands
import random
import os
import flask 
import keep_alive
description = '''Frost's discord bot.Prefix is ?'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
	activity = discord.Game(name="Bot getting verified, don't kick", type=3)
	await bot.change_presence(status=discord.Status.idle, activity=activity)
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')


@bot.command()
async def add(ctx, left: int, right: int):
	"""Adds two numbers together."""
	await ctx.send(left + right)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
	"""Chooses between multiple choices."""
	await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    if times >= 50:
      return await ctx.send("That is too much for me to handle! Try below 50.")
    elif times <= 0:
      return await ctx.send("Give me number of times in positive")
    for i in range(times):
      await ctx.send(content)


@bot.command(description='The classic 8Ball', aliases=['8ball'])
async def ask(ctx, *, question):
  await ctx.message.add_reaction("<a:React_8Ball:742587699453493288>")
  message = ctx.message.content.lower()
  list = ["will", "how", "why","is" ,
  "when", "where", "who", "whom","I","@","can","am","should","are","were","if","did","does","do"]
  bool = False
  for x in list:
    if x in message.split():
      bool = True
  if bool == False:
    return await ctx.send("Invalid question format.")
  await ctx.send(
	  random.choice([
	        "It is certain :8ball:", "It is decidedly so :8ball:",
	        "Without a doubt :8ball:", "Yes, definitely :8ball:",
	        "You may rely on it :8ball:", "As I see it, yes :8ball:",
	        "Most likely :8ball:", "Outlook good :8ball:", "Yes :8ball:",
	        "Signs point to yes :8ball:", "Reply hazy try again :8ball:",
	        "Ask again later :8ball:", "Better not tell you now :8ball:",
	        "Cannot predict now :8ball:", "Concentrate and ask again :8ball:",
	        "Don't count on it :8ball:", "My reply is no :8ball:",
	        "My sources say no :8ball:", "Outlook not so good :8ball:",
	        "Very doubtful :8ball:"
	    ]))

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title="Guild join", description=guild.name, color = 0x00FF00)
    count = 0
    for x in guild.members:
      count += 1
    placehold = '‎‎‎A'
    embed.add_field(name=f"Members: {count}", value=placehold)
    embed.add_field(name=f"Owner: {guild.owner}", value=placehold)
    a = bot.get_guild(742330503969112074)
    channel = a.get_channel(743028426927243366)
    await channel.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
    embed = discord.Embed(title="Guild leave", description=guild.name, color = 0xFF0000)
    count = 0
    for x in guild.members:
      count += 1
    placehold = 'A'
    embed.add_field(name=f"Members: {count}", value=placehold)
    embed.add_field(name=f"Owner: {guild.owner}", value=placehold)
    a = bot.get_guild(742330503969112074)
    channel = a.get_channel(743028426927243366)
    await channel.send(embed=embed)

embed = discord.Embed(
    title="Magic 8 Ball",
    description=
    "This bot solves your questions and more. For more questions do ?help. Also be sure to invite the bot!"
)
embed.colour = 0x00FFFF
embed.set_image(
    url=
    "https://cdn.discordapp.com/attachments/437067256049172491/742326962160271380/image0.png"
)
embed.add_field(name="Bot Dev", value="Frosty Boi#3293", inline=False)
embed2 = discord.Embed(
    title="Magic 8 Ball Help Page",
    description="Here is the list of commands for this server")
embed2.colour = 0x00FFFF
embed2.add_field(name="Help", value="Displays this command", inline=False)
embed2.add_field(
    name="About", value="Shows information about the bot ", inline=False)
embed2.add_field(
    name="Invite", value="Displays the bot's invite link ", inline=False)
embed2.add_field(name="Support", value="Sends the invite for the bot's support server ", inline=False)
embed2.add_field(name="Repeat", value="Repeats a phrase many times *Number of times comes first*", inline=False)
embed2.add_field(name="Ask", value="Asks Magic 8 Ball a question", inline=False)
embed2.add_field(name="Add", value="Adds numbers for you(When you are too dumb to do it yourself)", inline=False)
embed2.add_field(name="Choose", value="Chooses between two choices", inline=False)
@bot.command(description='Invite link')
async def invite(ctx):
	await ctx.send(
	    "https://discord.com/oauth2/authorize?client_id=742254708000817193&scope=bot&permissions=0"
	)


bot.remove_command('help')


@bot.command(description='Help')
async def help(ctx):
	await ctx.send(embed=embed2)


@bot.command(description='About the bot(Not help)')
async def about(ctx):
	await ctx.send(embed=embed)
keep_alive.run()
bot.run(os.environ.get("token"))
