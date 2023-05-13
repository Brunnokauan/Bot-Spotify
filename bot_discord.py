import discord
from discord import app_commands
from main import top_five
import os
from time import sleep

token_bot = os.getenv('TOKEN_BOT')

saudacoes = ['oi', 'Oi', 'olá', 'Olá']

class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1077791239732199575))
        print(f'Logged on as {self.user}')


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == 'top5':
            await message.channel.send(top_five())
        elif message.content in saudacoes:
            await message.channel.send('Olá, estranho!')
            sleep(2)
            await message.channel.send('É novo por aqui?')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

tree = app_commands.CommandTree(client)
# Digita comando
@tree.command(guild=discord.Object(id=1077791239732199575), name='top5', description='Top 5 músicas mais ouvidas deste mês')
async def top5(interaction: discord.Interaction):
    await interaction.response.send_message(top_five(), ephemeral=True)

# Seleciona comando. OBS: clique botão direito minha mensagem, em apps
# @tree.context_menu(name="Teste", guild=discord.Object(id=1077791239732199575))
# async def teste(interaction: discord.Interaction, message:discord.Message):
#     await interaction.response.send_message(f"Estou funcionando!")

client.run(token_bot)