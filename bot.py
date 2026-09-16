import os
import discord
import requests
import json
from dotenv import load_dotenv

# Carga el token desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Bot conectado con éxito como: {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        if message.content.startswith('$meme'):
            async with message.channel.typing():
                meme_url = get_meme()
                await message.channel.send(meme_url)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)