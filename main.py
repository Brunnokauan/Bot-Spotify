from access import web_api, autorization
import os

# def save_playlist():
#     tracksURI = ['spotify:track:4Bb53fsDAero14LpAbsmft','spotify:track:6f0XqZKDhD5EOTziuKYyq1','spotify:track:2CgOd0Lj5MuvOqzqdaAXtS','spotify:track:6wLujYsftQ9tGIvf54lrkz','spotify:track:3gB0fkEzOzV0kEWuQBFweu','spotify:track:4tAMNBZRoR2WQ6UnZs3Uuh','spotify:track:42xnrDAQcU0208y6iGR5Ls','spotify:track:6GiQfK7gtNGlODn53HZvpw','spotify:track:5kvFBu6jDJMECOqmD7OwUx','spotify:track:7fcLynQO9FrmYMOWuo1c1X']

#     token = autorization()
#     id =  web_api(token, 'v1/me', 'GET')

#     body = {
#         "name": "My recommendation playlist",
#         "description": "Playlist created by the tutorial on developer.spotify.com",
#         "public": False
#     }

#     playlist = web_api(token, f"v1/users/{id['id']}/playlists", 'POST', body)

#     try:
#         web_api(token, f"v1/playlists/{playlist['id']}/tracks?uris={','.join(tracksURI)}", 'POST')

#         print(f"{playlist['name']}, {playlist['id']}")
#         print('Playlist com músicas recomendadas criada.')
#     except:
#         print('Erro ao criar a playlist.')

# def device_list():
#     token = autorization('bru09')
#     id_dispositivo = None
#     res = web_api(token, "v1/me/player/devices", 'GET')
#     for a in enumerate(res['devices']):
#         print(a)
#         # if a['type'] == 'Computer':
#         #     id_dispositivo = resp['devices'][0]['id']
#         # elif a['type'] == 'Smartphone':
#         #     id_dispositivo = resp['devices'][0]['id']
#         # elif a['type'] == 'Iphone':
#         #     id_dispositivo = resp['devices'][0]['id']
#     # print(resp['devices'][0])
# device_list()

def listen_songs(songs:list, discord_user):
    token = autorization(discord_user)
    # body_example = {
    #     # "context_uri":"spotify:playlist:7fcLynQO9FrmYMOWuo1c1X", # playlist, album ou artista
    #     "uris": songs, # Faixas para reproduzir
    #     # "offset": {
    #     #     "position": 5 # ou "uri": "spotify:track:7fcLynQO9FrmYMOWuo1c1X"
    #     # },
    #     "position_ms": 0 # tempo que inicia a música
    # }

    body = {
        "uris": songs,
        "position_ms": 0
    }

    # try:
        # print(body)
    web_api(token, f"v1/me/player/play", 'PUT', body)
        # return 'Play músicas!'
    # except:
    #     print("Erro ao repoduzir.")
    # return 'Começa a tocar música.'

def top_songs(qtd_songs, discord_user):
    token = autorization(discord_user)
    top_tracks = web_api(token, f'v1/me/top/tracks?time_range=short_term&limit={qtd_songs}', 'GET')
    result = ''
    songs = []
    # try:
    for n, song in enumerate(top_tracks['items']):
        formater_song = f"spotify:track:{song['id']}"
        music = f"{n+1}. {song['name']} - " 
        artist = ''
        for a, artists in enumerate(top_tracks['items'][n]['artists']):
            if a+1 != len(top_tracks['items'][n]['artists']):
                text1 = f"{artists['name']}, " 
            else:
                text1 = f"{artists['name']}" 
            artist += text1
        result += music + artist
        songs.append(formater_song)
        if n != qtd_songs-1:
            result += os.linesep
        # print(song['artists'][0]['name'])
    listen_songs(songs, discord_user)
    return f'**TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS:**{os.linesep}' + result
    # except:
    #     return 'Não há músicas.'

def recomendation(qtd_songs, discord_user):
    token = autorization(discord_user)
    top_songs = web_api(token, f'v1/me/top/tracks?time_range=short_term&limit={qtd_songs}', 'GET')
    songs = []
    for song in top_songs['items']:
        song_id = f"{song['id']}"
        songs.append(song_id)

    new_songs = web_api(token, f"v1/recommendations?limit={qtd_songs}&seed_tracks={','.join(songs)}", 'GET')

    # for n, song in enumerate(new_songs['tracks']):
    #     print(f"{n+1}. {song['name']} by ", end='')
    #     for artists in new_songs['tracks'][n]['artists']:
    #         print(f"{artists['name']}",end=', ')
    #     print('\n', end='')
    
    result = ''
    for n, song in enumerate(new_songs['tracks']):
        music = f"{n+1}. {song['name']} - " 
        artist = ''
        for a, artists in enumerate(new_songs['tracks'][n]['artists']):
            if a+1 != len(new_songs['tracks'][n]['artists']):
                text1 = f"{artists['name']}, " 
            else:
                text1 = f"{artists['name']}" 
            artist += text1
        result += music + artist
        if n != qtd_songs-1:
            result += os.linesep
        # print(song['artists'][0]['name'])
    
    return f'**{qtd_songs} MÚSICAS RECOMENDADAS PARA VOÇÊ:**{os.linesep}' + result

def pause_songs():
    token = autorization()
    try:
        res = web_api(token, f"v1/me/player/pause", 'PUT')
        if res == 204:
            return 'Música pausada'
    except:
        print(ValueError)

def playback_shuflle():
    token = autorization()
    res = web_api(token, f"v1/me/player/shuffle?state=true", 'PUT')
    if res == 204:
        return 'Músicas em modo aleatório ativado.'
    
# def get_status_playback():
#     token = autorization('bru09')
#     res = web_api(token, f"v1/me/player/currently-playing", 'GET')
#     print(res)
# get_status_playback()