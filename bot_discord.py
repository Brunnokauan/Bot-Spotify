import discord
from discord import app_commands
from main import top_songs, listen_songs, pause_songs, playback_shuflle
from access import autorization
import os
from dotenv import load_dotenv

load_dotenv()

token_bot = os.getenv('TOKEN_BOT')
id_servidor = os.getenv('SERVIDOR_ID')

class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=id_servidor))
        print(f'Logged on as {self.user}')


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        # if message.content == 'top5':
        #     await message.channel.send(top_five())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

tree = app_commands.CommandTree(client)
# Digita comando
@tree.command(guild=discord.Object(id=id_servidor), name='top-songs', description='Top músicas mais ouvidas deste mês. Padrão: 5')
async def topSongs(interaction: discord.Interaction, qtd:int=5):
    user = interaction.user.display_name
    print(f'Message from {user}: /top-songs')  
    await interaction.response.send_message(top_songs(qtd, user), ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name='play', description='Tocar uma playlist ou álbum.')
async def playSongs(interaction: discord.Interaction, playlist:str=None, album:str=None):
    await interaction.response.send_message(listen_songs(), ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name='pause', description='Pausa a música.')
async def playSongs(interaction: discord.Interaction):
    await interaction.response.send_message(pause_songs(), ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name='playback-shuffle', description='Toca de modo aleatório.')
async def playSongs(interaction: discord.Interaction):
    await interaction.response.send_message(playback_shuflle() ,ephemeral=True)

# Seleciona comando. OBS: clique botão direito minha mensagem, em apps
# @tree.context_menu(name="Teste", guild=discord.Object(id=id_servidor))
# async def teste(interaction: discord.Interaction, message:discord.Message):
#     await interaction.response.send_message(f"Estou funcionando!")
client.run(token_bot)