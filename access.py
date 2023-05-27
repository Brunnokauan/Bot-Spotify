# import spotipy.util as util
# from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
# import spotipy
import requests
import mysql.connector
import base64
# import json

# def autorization(discord_user:str):
#     username = 'bot-spotify'
#     redirect_uri = 'http://localhost:8888/callback'
#     scope = 'user-top-read playlist-modify-private user-modify-playback-state user-read-playback-state'

#     load_dotenv()

#     client_id = os.getenv("CLIENT_ID")
#     client_secret = os.getenv("CLIENT_SECRET")
#     cache_path = f'cache/cache-{discord_user}'

#     # token = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
#     token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, cache_path=cache_path)
#     return token

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
database = os.getenv("DATABASE")

def register_user(user_discord:str, token:str, refresh_token:str):
    try:
        cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        sql = f'INSERT INTO user_discord (display_name, access_token, refresh_token, created_at, updated_at) VALUES (\"{user}\", \"{token}\", \"{refresh_token}\", NOW(), NOW())'
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        cursor.close()
        cnx.close()
        return f'Usuário {user_discord} registrado com sucesso!'
    except:
        return 'Erro ao registrar usuário.'

def refresh_token(user:str):
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    cursor = cnx.cursor()
    query = f'SELECT refresh_token FROM user_discord WHERE display_name=\"{user}\"'
    cursor.execute(query)

    for token in cursor:
        refresh_token = token[0]

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    headers = {"Authorization": f"Basic {auth_base64}", "Content-Type": "application/x-www-form-urlencoded"}
    body = {
        "grant_type": 'refresh_token',
        "refresh_token": refresh_token
    }

    res = requests.post(url='https://accounts.spotify.com/api/token', headers=headers, data=body)
    # json_result = json.loads(res.content)
    # token = json_result

    query2 = f"UPDATE user_discord SET access_token=\"{res.json()['access_token']}\", updated_at=NOW() WHERE display_name=\"{user}\""
    cursor.execute(query2)
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return res.json()['access_token']

def autorization(user:str):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bot')
    cursor = cnx.cursor()

    query = f'SELECT access_token FROM user_discord WHERE display_name=\"{user}\"'

    cursor.execute(query)

    for token in cursor:
        access_token = token[0]
    
    cursor.close()
    cnx.close()
    try:
        return access_token
    except:
        return None
# autorization('teste')

def web_api(token, endpoint, method, body=None):
    # data = {"grant_type": "client_credentials"}
    if (method == 'GET'):
        res = requests.get(url=f"https://api.spotify.com/{endpoint}", headers={"Authorization": f"Bearer {token}"})
        return res.json()
    elif (method == 'POST'):
        res = requests.post(url=f"https://api.spotify.com/{endpoint}",
              headers={"Authorization": f'Bearer {token}', "Content-Type": "application/json"},
              json=body)
        return res.json()
    elif (method == 'PUT'):
        if body != None:
            res = requests.put(url=f"https://api.spotify.com/{endpoint}",
              headers={"Authorization": f'Bearer {token}', "Content-Type": "application/json"},
              json=body)
        else:
            res = requests.put(url=f"https://api.spotify.com/{endpoint}",
              headers={"Authorization": f'Bearer {token}'})
        return res.status_code

# result = web_api('v1/me','get')
# print(result)