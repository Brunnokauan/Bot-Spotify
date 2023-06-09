top_tracks = list()
recomendations_tracks = list()
specific_track = list()

def post_top_musics(songs:list):
    top_tracks.clear()
    for m in songs:
        top_tracks.append(m)

def post_recomendations_musics(songs:list):
    recomendations_tracks.clear()
    for m in songs:
        recomendations_tracks.append(m)

def post_track(songs:list):
    specific_track.clear()
    for m in songs:
        specific_track.append(m)
