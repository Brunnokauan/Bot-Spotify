from access import web_api, refresh_token
from access import authorization
import discord

def duration_music(ms:int):
    minutos = ms//60000
    segundos = str((ms%60000)//1000)

    if len(segundos) == 1:
        segundos = '0' + f'{segundos}'

    return f'{minutos}:{segundos}'

def formater_embed(titulo:str, descricao:str, tracks:list):
    embed = discord.Embed(
        title=titulo,
        description=descricao,
        color=discord.Colour.light_embed(),
    )
    for info in tracks:
        embed.add_field(name=info['name'],value=info['value'], inline=False)
    return embed

def listen_songs(token, songs:list):
    body = {
        "uris": songs,
        "position_ms": 0
    }

    try:
        res = web_api(token, f"v1/me/player/play", "PUT", body)
        if res == 204:
            return "Play music!"
    except:
        return "Erro ao repoduzir."

def top_songs(token, qtd_songs):
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
            tracks.append({'name': music, 'value': artist})
            songs.append(formater_song)
        return formater_embed(
            titulo=f'TOP {qtd_songs} MÚSICAS MAIS OUVIDAS DESTE MÊS',
            descricao='As suas mais ouvidas nesse mês',
            tracks=tracks
        ), songs
    except:
        return "Não há músicas."

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
        tracks_id.append(formater_track)
    embed = formater_embed(
        titulo=f'{qtd_songs} MÚSICAS RECOMENDADAS PARA VOCÊ',
        descricao='Músicas recomendadas a partir das top músicas',
        tracks=tracks
    )
    return embed, tracks_id

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

def search_music(token, q:str):
    try:
        q.replace(' ','+')
        res = web_api(token, f"v1/search?q={q}&type=track&limit=5", "GET")
        tracks = []
        tracks_id = []
        for n, info in enumerate(res['tracks']['items']):
            music = f"{n+1}. {info['name']}"
            artists = ''
            for n2, info2 in enumerate(res['tracks']['items'][n]['artists']):
                if n2+1 != len(res['tracks']['items'][n]['artists']):
                    a = f"{info2['name']}, "
                else:
                    a = f"{info2['name']} - "
                artists += a
            tracks.append({'name':music, 'value': artists + duration_music(info['duration_ms'])})
            tracks_id.append(info['uri'])
        return formater_embed(
            titulo=f'MÚSICAS: {q}',
            descricao='Busca uma determinada música',
            tracks=tracks
        ), tracks_id
    except:
        return 'Erro ao encontrar a música.'
