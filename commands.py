from access import web_api, authorization, refresh_token
import os

def listen_songs(songs:list, discord_user):
    token = authorization(discord_user)

    body = {
        "uris": songs,
        "position_ms": 0
    }

    try:
        res = web_api(token, f"v1/me/player/play", 'PUT', body)
        if res == 204:
            return "Play music!"
        else:
            token = refresh_token(discord_user)
            res = web_api(token, f"v1/me/player/play", 'PUT', body)
            if res == 204:
                return "Play music!"
    except:
        return "Erro ao repoduzir."

def top_songs(qtd_songs, discord_user:str):
    token = authorization(discord_user)
    result = ''
    songs = []
    try:
        top_tracks = web_api(token, f"v1/me/top/tracks?time_range=short_term&limit={qtd_songs}", "GET")
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
        return f"**TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS:**{os.linesep}" + result
    except KeyError:
        token = refresh_token(discord_user)
        top_tracks = web_api(token, f"v1/me/top/tracks?time_range=short_term&limit={qtd_songs}", "GET")
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
        return f"**TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS:**{os.linesep}" + result
    except:
        return "Não há músicas."
# print(top_songs(5, 'Lukitas25'))

def recomendation(token, qtd_songs, discord_user):
    top_songs = web_api(token, f"v1/me/top/tracks?time_range=short_term&limit={qtd_songs}", "GET")
    songs = []
    for song in top_songs['items']:
        song_id = f"{song['id']}"
        songs.append(song_id)

    new_songs = web_api(token, f"v1/recommendations?limit={qtd_songs}&seed_tracks={','.join(songs)}", 'GET')
    
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
    
    return f"**{qtd_songs} MÚSICAS RECOMENDADAS PARA VOCÊ:**{os.linesep}" + result

def pause_songs(discord_user):
    token = authorization(discord_user)
    try:
        res = web_api(token, f"v1/me/player/pause", 'PUT')
        if res == 204:
            return "Música pausada"
        else:
            token = refresh_token(discord_user)
            res = web_api(token, f"v1/me/player/pause", 'PUT')
            if res == 204:
                return "Música pausada"
    except:
        return "Erro ao pausar a música"

def playback_shuflle(discord_user):
    token = authorization(discord_user)
    try:
        res = web_api(token, f"v1/me/player/shuffle?state=true", 'PUT')
        if res == 204:
            return "Músicas em modo aleatório ativado."
        else:
            token = refresh_token(discord_user)
            res = web_api(token, f"v1/me/player/shuffle?state=true", 'PUT')
            if res == 204:
                return "Músicas em modo aleatório ativado."
    except:
        return "Erro ao ativar lista de reprodução aleatória."