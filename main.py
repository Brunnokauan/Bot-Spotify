from access import web_api
import os

def top_five():
    top_tracks = web_api('v1/me/top/tracks?time_range=short_term&limit=5','get', '')
    result = ''
    for n, song in enumerate(top_tracks['items']):
        text = f"{n+1}. {song['name']} by {song['artists'][0]['name']}{os.linesep}"
        result += text
        # print(song['artists'][0]['name'])

    return result

# top_tracks = top_five()
# print(top_tracks['items'][0]['artists'])
# for n, song in enumerate(top_tracks['items']):
#     # print(f"{n+1}. {song['name']} by {song['artists'][0]['name']}")
#     print(song['artists'][0]['name'])
