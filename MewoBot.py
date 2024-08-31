
import os
import random
import discord
from dotenv import load_dotenv
intents = discord.Intents.all()
realcount = 1
LoveEmojis = [":catKiss:1151574950168231946",
":headpats:1151574617014681720",
":headpatCat:1158800541447630908",
":menheraHappy:1158800544266211358",
":up_cute:1140993882528690347>",
":lovehearts:1229447179450454158",
":happy:1229446842111234099",
":love:1229447177462616097",
":menherakiss:1229446837744828587"]

swearEmojis = ["😡", "❗", ":highmelfstare:1229454592606081055"]

from songlists import songs # type: ignore
swearlist = ["fuck", "bitch", "shit", "cunt", "frick", "damn", "crap", "hell", "british"]


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client(intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0
	

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("MewoBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):

	if message.content.lower().replace(" ", "") == "real":
		global realcount
		if random.randint(0,100) > 80:
			user = await bot.fetch_user("1138462287183749200")
			message = "<@113846228718374920>" + " " + str(realcount)
			await user.send("<@1138462287183749200>")
			print("real", realcount)
			realcount += 1
		
	if message.content.lower() == "give me a will wood song" and message.channel.id == 1141727040932954152 or message.content.lower() == "give me a will wood song" and message.channel.id == 1229175077585686658:
		await message.channel.send(random.choice(songs))
	elif message.content.lower() == "mewo" and message.channel.id == 1141727040932954152 or message.content.lower() == "mewo" and message.channel.id == 1229175077585686658:
		emoji = ":mewo:1173019944695369799"
		await message.add_reaction(emoji)
	for i in swearlist:
		if i in message.content.lower() and message.channel.id == 1141727040932954152:
			await message.add_reaction(random.choice(swearEmojis))

	if message.author.id == 1138462287183749200 or message.author.id == 311700174260928513:
		global LoveEmojis
		await message.add_reaction(random.choice(LoveEmojis))



bot.run(TOKEN)	

