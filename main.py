from access import web_api

def top_five():
    result = web_api('v1/me/top/tracks?time_range=short_term&limit=5','get', '')
    return result

top_tracks = top_five()
print(top_tracks)
# for name, artist in top_tracks:
#     print(f'{name} by', end=' ')
#     for artists in artist:
#         print(','.join(artists.name))
