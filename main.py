from access import web_api
import os

def top_five(qtd_songs):
    top_tracks = web_api(f'v1/me/top/tracks?time_range=short_term&limit={qtd_songs}','get', None)
    result = ''
    for n, song in enumerate(top_tracks['items']):
        music = f"{n+1}. {song['name']} - " 
        artist = ''
        for a, artists in enumerate(top_tracks['items'][n]['artists']):
            if a+1 != len(top_tracks['items'][n]['artists']):
                text1 = f"{artists['name']}, " 
            else:
                text1 = f"{artists['name']}" 
            artist += text1
        result += music + artist
        if n != qtd_songs-1:
            result += os.linesep
        # print(song['artists'][0]['name'])
    return f'**TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS:**{os.linesep}' + result

def recomendation():
    topTracksIds = ['4Bb53fsDAero14LpAbsmft','2CgOd0Lj5MuvOqzqdaAXtS','3gB0fkEzOzV0kEWuQBFweu','42xnrDAQcU0208y6iGR5Ls','5kvFBu6jDJMECOqmD7OwUx']

    new_songs = web_api(f"v1/recommendations?limit=5&seed_tracks={','.join(topTracksIds)}", 'get', None)

    for n, song in enumerate(new_songs['tracks']):
        print(f"{n+1}. {song['name']} by ", end='')
        for artists in new_songs['tracks'][n]['artists']:
            print(f"{artists['name']}",end=', ')
        print('\n', end='')

def save_playlist():
    tracksURI = ['spotify:track:4Bb53fsDAero14LpAbsmft','spotify:track:6f0XqZKDhD5EOTziuKYyq1','spotify:track:2CgOd0Lj5MuvOqzqdaAXtS','spotify:track:6wLujYsftQ9tGIvf54lrkz','spotify:track:3gB0fkEzOzV0kEWuQBFweu','spotify:track:4tAMNBZRoR2WQ6UnZs3Uuh','spotify:track:42xnrDAQcU0208y6iGR5Ls','spotify:track:6GiQfK7gtNGlODn53HZvpw','spotify:track:5kvFBu6jDJMECOqmD7OwUx','spotify:track:7fcLynQO9FrmYMOWuo1c1X']
    id =  web_api('v1/me', 'get', None)

    body = {
        "name": "My recommendation playlist",
        "description": "Playlist created by the tutorial on developer.spotify.com",
        "public": False
    }

    playlist = web_api(f"v1/users/{id['id']}/playlists", 'post', body)

    try:
        web_api(f"v1/playlists/{playlist['id']}/tracks?uris={','.join(tracksURI)}", 'post', None)

        print(f"{playlist['name']}, {playlist['id']}")
        print('Playlist com músicas recomendadas criada.')
    except:
        print('Erro ao criar a playlist.')

def listen_songs():
    id_disposivo = 0

    body = {
        "context_uri":"spotify:track:7fcLynQO9FrmYMOWuo1c1X", # playlist, album ou artista
        # "uris": ["spotify:track:7fcLynQO9FrmYMOWuo1c1X", "spotify:track:7fcLynQO9FrmYMOWuo1c1X"], Faixas para reproduzir
        # "offset": {
        #     "position": 5 # ou "uri": "spotify:track:7fcLynQO9FrmYMOWuo1c1X"
        # },
        "position_ms": 0 # tempo que inicia a música
    }

    try:
        web_api(f"v1/me/player/play", 'put', body)
    except:
        print("Erro ao repoduzir.")    

