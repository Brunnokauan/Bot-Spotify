import discord
from discord import app_commands
from discord.ext import commands
from commands import top_songs, pause_songs, playback_shuflle, recomendation, search_music
from access import register_user, authorization
import os
from dotenv import load_dotenv

load_dotenv()

token_bot = os.getenv("TOKEN_BOT")
id_servidor = os.getenv("SERVIDOR_ID")
error_message = """Não encontrei você nos meus dados. Você pode se registrar acessando esse link: https://authorization-bot-spotify-homologation.up.railway.app/"""

class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=id_servidor))
        print(f"Logged on as {self.user}")


    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        # if message.content == 'top5':
        #     await message.channel.send(top_five())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# client2 = commands.Bot(command_prefix = '/', intents=intents)

# client2.command()
# async def embed(ctx):
    
#     await ctx.send(embed = embedTest)

tree = app_commands.CommandTree(client)
# Digita comando
@tree.command(guild=discord.Object(id=id_servidor), name="register", description="Registra seu usuário.")
async def register(interaction: discord.Interaction, access_token:str, refresh_token:str):
    user = interaction.user.display_name
    print(f"Message from {user}: /register")  
    await interaction.response.send_message(register_user(user, access_token, refresh_token), ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name="top-songs", description="Top músicas mais ouvidas deste mês. Padrão: 5")
async def topSongs(interaction: discord.Interaction, qtd:int=5):
    user = interaction.user.display_name
    print(f"Message from {user}: /top-songs")
    token = authorization(user)
    if token == None:
        await interaction.response.send_message(error_message ,ephemeral=True)
    else:  
        await interaction.response.send_message(top_songs(token, qtd, user), ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name='play', description='Toca uma música especifica.')
async def playSongs(interaction: discord.Interaction, music:str):
    user = interaction.user.display_name
    await interaction.response.send_message(search_music(music, user))
    
@tree.command(guild=discord.Object(id=id_servidor), name="pause", description="Pausa a música.")
async def pauseSong(interaction: discord.Interaction):
    user = interaction.user.display_name
    print(f"Message from {user}: /pause") 
    token = authorization(user)
    if token == None:
        await interaction.response.send_message(error_message ,ephemeral=True)
    else:
        await interaction.response.send_message(pause_songs(token, user), ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name="playback-shuffle", description="Toca de modo aleatório.")
async def playbackShuffle(interaction: discord.Interaction):
    user = interaction.user.display_name
    print(f"Message from {user}: /playback-shuffle")
    token = authorization(user)
    if token == None:
        await interaction.response.send_message(error_message ,ephemeral=True)
    else: 
        await interaction.response.send_message(playback_shuflle(token, user) ,ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name="recomendation-songs", description="Recomendações de músicas baseadas nos seus topSongs. Padrão: 5")
async def recomandationsSongs(interaction: discord.Interaction, qtd:int=5):
    user = interaction.user.display_name
    print(f"Message from {user}: /recomendation-songs")
    token = authorization(user)
    if token == None:
        await interaction.response.send_message(error_message ,ephemeral=True)
    else:
        await interaction.response.send_message(recomendation(token, qtd, user) ,ephemeral=True)

@tree.command(guild=discord.Object(id=id_servidor), name="embeds", description="Mostra como seria um embed")
async def embed(interaction: discord.Interaction):
    user = interaction.user.display_name
    print(f"Message from {user}: /embed")
    embedTest = discord.Embed(
        title='Titulo',
        description='Descrição do Embed',
        color=discord.Colour.light_embed()
    )
    await interaction.response.send_message(embed=embedTest ,ephemeral=True)
    

client.run(token_bot)