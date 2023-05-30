import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
# import spotipy.util as util
# from spotipy.oauth2 import SpotifyOAuth
# import spotipy
# import json

# data = {"grant_type": "client_credentials"}

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
port = os.getenv("PORT")
redirect_uri = f'http://{port}/callback'
scope = 'user-top-read'
sp = spotipy.Spotify(oauth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))
# sp = spotipy.Spotify(oauth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, cache_handler=spotipy.CacheFileHandler(username='bru09' )))

ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=5)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    print()

# main.py
# Seleciona comando. OBS: clique botão direito minha mensagem, em apps
# @tree.context_menu(name="Teste", guild=discord.Object(id=id_servidor))
# async def teste(interaction: discord.Interaction, message:discord.Message):
#     await interaction.response.send_message(f"Estou funcionando!")

# commands.py - listen_songs()
# body_example = {
    #     # "context_uri":"spotify:playlist:7fcLynQO9FrmYMOWuo1c1X", # playlist, album ou artista
    #     "uris": songs, # Faixas para reproduzir
    #     # "offset": {
    #     #     "position": 5 # ou "uri": "spotify:track:7fcLynQO9FrmYMOWuo1c1X"
    #     # },
    #     "position_ms": 0 # tempo que inicia a música
    # }

# commands.py
# def teste(user:str):
#     cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bot')
#     cursor = cnx.cursor()

#     query = f'SELECT access_token FROM user_discord WHERE display_name=\"{user}\"'

#     cursor.execute(query)

#     for token in cursor:
#         access_token = token[0]
    
#     cursor.close()
#     cnx.close()
#     print(access_token)

# teste('bru09')

# def get_status_playback():
#     token = autorization('bru09')
#     res = web_api(token, f"v1/me/player/currently-playing", 'GET')
#     print(res)
# get_status_playback()