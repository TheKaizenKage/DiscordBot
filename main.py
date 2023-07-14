#Libraries used
import discord
from discord.ext import commands
import random as rd

"""
Information needed:
Discord Bot token : MTEyOTIxNjEyMzg0MjMzNDg1MQ.Gnsvor.OgFN8mB951ZsBnSWFHZiypLJf-X6AUjR4_ROvU
"""

#Intent is the type of content we are interacting with. In our case we want all of them cuz why not :D
intent = discord.Intents.all()

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='/',intents=intent)

# Event: Bot is ready and connected to the server
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

# Event: Capture a user's message
@bot.event
async  def on_message(message):
    value = rd.randint(0,7)
    if message.author == bot.user:
        return
    match value:
        case 0:
            await message.channel.send("SOOO YOU SEE?")

        case 1:
            await message.channel.send("Never judge a book by its cover")

        case 2:
             await message.channel.send("Always remember, we're not just telling stories, we're changing lives.")

        case 3:
            await message.channel.send("It's not about what you have, but what you do with what you have.")

        case 4:
            await message.channel.send("Kindness costs nothing but means everything.")

        case 5:
             await message.channel.send("Believe in yourself and your dreams; anything is possible.")

        case 6:
            await message.channel.send("Hard work and perseverance are the keys to success.")


bot.run('MTEyOTIxNjEyMzg0MjMzNDg1MQ.Gnsvor.OgFN8mB951ZsBnSWFHZiypLJf-X6AUjR4_ROvU')


