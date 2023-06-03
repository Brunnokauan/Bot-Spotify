from access import web_api, refresh_token
import os
# from access import authorization

def listen_songs(token, songs:list, discord_user):
    body = {
        "uris": songs,
        "position_ms": 0
    }

    try:
        res = web_api(token, f"v1/me/player/play", "PUT", body)
        if res == 204:
            return "Play music!"
        else:
            token = refresh_token(discord_user)
            res = web_api(token, f"v1/me/player/play", "PUT", body)
            if res == 204:
                return "Play music!"
    except:
        return "Erro ao repoduzir."

def top_songs(token, qtd_songs, discord_user:str):
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
        listen_songs(token, songs, discord_user)
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
        listen_songs(token, songs, discord_user)
        return f"**TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS:**{os.linesep}" + result
    except:
        return "Não há músicas."
# print(top_songs(5, 'Lukitas25'))

def recomendation(token, qtd_songs, discord_user):
    try:
        top_songs = web_api(token, f"v1/me/top/tracks?time_range=short_term&limit=5", "GET")
        songs = []
        for song in top_songs['items']:
            song_id = f"{song['id']}"
            songs.append(song_id)
        # print(songs)

        new_songs = web_api(token, f"v1/recommendations?limit={qtd_songs}&seed_tracks={','.join(songs)}", "GET")
    except KeyError:
        token = refresh_token(discord_user)
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
    
    result = ''
    tracks_id = []
    for n, song in enumerate(new_songs['tracks']):
        formater_track = f"spotify:track:{song['id']}"
        music = f"{n+1}. {song['name']} - " 
        artist = ''
        for a, artists in enumerate(new_songs['tracks'][n]['artists']):
            if a+1 != len(new_songs['tracks'][n]['artists']):
                text1 = f"{artists['name']}, " 
            else:
                text1 = f"{artists['name']}" 
            artist += text1
        result += music + artist
        tracks_id.append(formater_track)
        if n != qtd_songs-1:
            result += os.linesep
        # print(song['artists'][0]['name'])
    
    listen_songs(token, tracks_id, discord_user)
    return f"**{qtd_songs} MÚSICAS RECOMENDADAS PARA VOCÊ:**{os.linesep}" + result
# token = authorization('bru09')
# print(recomendation(token, 5, 'bru09'))

def pause_songs(token, discord_user):
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

def playback_shuflle(token, discord_user):
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