# https://discord.com/oauth2/authorize?client_id=763983838476369961&permissions=51200&scope=bot
import sys, io
import os

from dotenv import dotenv_values
import discord

intents = discord.Intents.default()
bot = discord.Client(command_prefix="", intents=intents)

# When bot is ready to run
@bot.event
async def on_ready():
	print("Bot running...")

# Do something when a message is sent
@bot.event
async def on_message(message):
	try:
		message_id, content = message.content.split(' ')
		if content.startswith('!'):
			# @bot !about
			if content[1:].lower() == "about":
				text = ""
				with open("about.txt", 'r') as aboutfile:
					text = aboutfile.read()
				print(text)
				await message.channel.send(message.author.mention + " " + text)
			# @bot !emotional-damage
			elif content[1:].lower() == "emotional":
				await message.channel.send(message.author.mention + " **EMOTIONAL DAMAGE**", file=discord.File("assets/emotional.mp4"))
			# @bot !therapy
			elif content[1:].lower() == "therapy":
				await message.channel.send(message.author.mention + " *you want some therapy*", file=discord.File("assets/therapy.mp4"))
	except:
		pass

if __name__ == '__main__':
	# Run the bot
	config = dotenv_values(".env")
	bot.run(config["BOT_TOKEN"])
