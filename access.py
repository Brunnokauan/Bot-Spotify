import spotipy.util as util
# from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
# import spotipy
import requests

def autorization():
    username = 'bot-spotify'
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'user-top-read playlist-modify-private user-modify-playback-state user-read-playback-state'

    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    # token = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
    token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    return token

def web_api(token, endpoint, method, body=None):
    # data = {"grant_type": "client_credentials"}
    if (method == 'GET'):
        res = requests.get(url=f"https://api.spotify.com/{endpoint}", headers={"Authorization": f"Bearer {token}"})
    elif (method == 'POST'):
        res = requests.post(url=f"https://api.spotify.com/{endpoint}",
              headers={"Authorization": f'Bearer {token}', "Content-Type": "application/application/json"},
              json=body)
    elif (method == 'PUT'):
        res = requests.post(url=f"https://api.spotify.com/{endpoint}",
              headers={"Authorization": f'Bearer {token}', "Content-Type": "application/application/json"},
              json=body)
    return res.json()

# result = web_api('v1/me','get')
# print(result)