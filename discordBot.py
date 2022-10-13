BOTTOKEN = ''


import discord
from discord_components import *
import discord.ext.commands as commands
import json

client = commands.Bot("!")
DiscordComponents(client)

'''
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello, I am your Botler your personal butler bot')'''
@client.event
async def on_ready():
	print("The Bot {0.user} has logged in".format(client))
	print("--------------------------------")

@client.command()
async def old(ctx):
	await ctx.send("Whoaaa you are now 109", components = [
		[Button(label="Hi", style='3', emoji = '🎁', custom_id='button1'), Button(label="Bye", style='4', emoji='👋', custom_id="button2")]
		], delete_after=10)
	interaction = await client.wait_for("button_click", check = lambda i: i.custom_id == "button1")
	await ctx.message.delete()
	await interaction.send(content = 'Happy Birthday USER!', ephemeral=True)

@client.command()
async def message(ctx, user:discord.Member, *, message=None):
	message = "Testing 123"
	embed = discord.Embed(title=message)
	await user.send(embed=embed)

client.run(BOTTOKEN)
