import discord
import key

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in?")

@client.event
async def on_message(message):
        if message.author.global_name == key.raccoon_name:
              await message.reply(content=key.to_send)
              print(f'Did it')
    # print(message.author.id)
client.run(key.bot_token)