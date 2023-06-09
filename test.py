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

# commands.py
def top_songs(token, qtd_songs):
    result = ''
    songs = []
    try:
        top_tracks = web_api(token, f"v1/me/top/tracks?time_range=short_term&limit={qtd_songs}", "GET")
        tracks = []
        for n, song in enumerate(top_tracks['items']):
            formater_song = f"spotify:track:{song['id']}"
            music = f"{n+1}. {song['name']}" 
            artist = ''
            for a, artists in enumerate(top_tracks['items'][n]['artists']):
                if a+1 != len(top_tracks['items'][n]['artists']):
                    text1 = f"{artists['name']}, " 
                else:
                    text1 = f"{artists['name']}" 
                artist += text1
            # result += music + artist
            tracks.append({'name': music, 'value': artist})
            songs.append(formater_song)
            # if n != qtd_songs-1:
            #     result += os.linesep
            # print(song['artists'][0]['name'])
        # listen_songs(token, songs, discord_user)
        # return f"**TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS:**{os.linesep}" + result
        return formater_embed(
            titulo=f'TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS',
            descricao='As suas mais ouvidas nesse mês',
            tracks=tracks
        ), songs
    except:
        return "Não há músicas."
# print(top_songs(5, 'Lukitas25'))

def recomendation(token, qtd_songs):
    try:
        top_songs = web_api(token, f"v1/me/top/tracks?time_range=short_term&limit=5", "GET")
        songs = []
        for song in top_songs['items']:
            song_id = f"{song['id']}"
            songs.append(song_id)
        # print(songs)

        new_songs = web_api(token, f"v1/recommendations?limit={qtd_songs}&seed_tracks={','.join(songs)}", "GET")
    except:
        return "Erro em listar as músicas"

    # for n,id in enumerate(new_songs['tracks']):
    #     print(id['id'])
    #     print(new_songs['tracks'][n])
    
    # result = ''
    tracks_id = []
    tracks = []
    for n, song in enumerate(new_songs['tracks']):
        formater_track = f"spotify:track:{song['id']}"
        music = f"{n+1}. {song['name']}" 
        artist = ''
        for a, artists in enumerate(new_songs['tracks'][n]['artists']):
            if a+1 != len(new_songs['tracks'][n]['artists']):
                text1 = f"{artists['name']}, " 
            else:
                text1 = f"{artists['name']}" 
            artist += text1
        tracks.append({'name': music, 'value': artist})
        # result += music + artist
        tracks_id.append(formater_track)
        # if n != qtd_songs-1:
        #     result += os.linesep
        # print(song['artists'][0]['name'])
    
    # listen_songs(token, tracks_id, discord_user)
    embed = formater_embed(
        titulo=f'{qtd_songs} MÚSICAS RECOMENDADAS PARA VOCÊ',
        descricao='Músicas recomendadas a partir das top músicas',
        tracks=tracks
    )
    # return f"**{qtd_songs} MÚSICAS RECOMENDADAS PARA VOCÊ:**{os.linesep}" + result
    return embed, tracks_id
# token = authorization('bru09')
# print(recomendation(token, 5, 'bru09'))

def pause_songs(token):
    try:
        res = web_api(token, f"v1/me/player/pause", 'PUT')
        if res == 204:
            return "Música pausada"
    except:
        return "Erro ao pausar a música"

def playback_shuflle(token):
    try:
        res = web_api(token, f"v1/me/player/shuffle?state=true", 'PUT')
        if res == 204:
            return "Músicas em modo aleatório ativado."
    except:
        return "Erro ao ativar lista de reprodução aleatória."

# import os
def search_music(token, q:str):
    try:
        q.replace(' ','+')
        res = web_api(token, f"v1/search?q={q}&type=track&limit=5", "GET")
        tracks = []
        tracks_id = []
        result = ''
        for n,info in enumerate(res['tracks']['items']):
            music = f"{n+1}. {info['name']}"
            artists = ''
            for n2,info2 in enumerate(res['tracks']['items'][n]['artists']):
                if n2+1 != len(res['tracks']['items'][n]['artists']):
                    a = f"{info2['name']}, "
                else:
                    a = f"{info2['name']} - "
                artists += a
            tracks.append({'name':music, 'value': artists + duration_music(info['duration_ms'])})
            tracks_id.append(info['uri'])
        #     result += music + artists + duration_music(info['duration_ms'])
        #     if n < 4:
        #         result += os.linesep
        # print(tracks_id)
        # return result
        return formater_embed(
            titulo=f'MÚSICAS: {q}',
            descricao='Busca uma determinada música',
            tracks=tracks
        ), tracks_id
    except:
        return 'Erro ao encontrar a música.'
    
# print(search_music('only one', 'bru09'))