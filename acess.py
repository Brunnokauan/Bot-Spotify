import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

username = 'bot-spotify'
redirect_uri = 'http://localhost:8888/callback'
scope = 'user-read-recently-played'

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# token = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

print(client_id)
input()