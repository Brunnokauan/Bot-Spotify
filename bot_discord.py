import discord
from main import top_five
import os
from dotenv import load_dotenv

token_bot = os.getenv('TOKEN_BOT')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == 'top5':
            await message.channel.send(f'Top 5 músicas deste mês:{os.linesep}{os.linesep}' + top_five())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token_bot)