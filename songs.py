top_tracks = [{}]
recomendations_tracks = [{}]
specific_track = [{}]


def post_top_musics(songs:list, user_discord):
    # top_tracks.clear()
    # for m in songs:
    #     top_tracks.append(m)
    if (user_discord in top_tracks[0]) == True:
        print('usuário encontrado!')
        top_tracks[0][user_discord] = songs        
    else:
        top_tracks[0][user_discord] = songs

def post_recomendations_musics(songs:list, user_discord):
    if (user_discord in recomendations_tracks[0]) == True:
        print('usuário encontrado!')
        recomendations_tracks[0][user_discord] = songs        
    else:
        recomendations_tracks[0][user_discord] = songs

def post_track(songs:list, user_discord):
    if (user_discord in specific_track[0]) == True:
        print('usuário encontrado!')
        specific_track[0][user_discord] = songs        
    else:
        specific_track[0][user_discord] = songs

def get_top_musics(user_discord:str):
    return top_tracks[0][user_discord]

def get_recomendations_musics(user_discord:str):
    return recomendations_tracks[0][user_discord]

def get_track(user_discord:str):
    return specific_track[0][user_discord]
