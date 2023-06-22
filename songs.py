top_tracks = [{}]
recomendations_tracks = [{}]
specific_track = [{}]

# Função resposável por guardar top-músicas do usuário com seus indentificadores caso o clique no botão tocar música.
def post_top_musics(songs:list, user_discord):
    if (user_discord in top_tracks[0]) == True:
        print('usuário encontrado!')
        top_tracks[0][user_discord] = songs        
    else:
        top_tracks[0][user_discord] = songs

# Função resposável por guardar músicas recomendadas do usuário com seus indentificadores caso o clique no botão tocar música.
def post_recomendations_musics(songs:list, user_discord):
    if (user_discord in recomendations_tracks[0]) == True:
        print('usuário encontrado!')
        recomendations_tracks[0][user_discord] = songs        
    else:
        recomendations_tracks[0][user_discord] = songs

#Função resposável por guardar músicas buscadas no comando play com seus indentificadores, caso clique em um dos botões para tocar uma música
def post_track(songs:list, user_discord):
    if (user_discord in specific_track[0]) == True:
        print('usuário encontrado!')
        specific_track[0][user_discord] = songs        
    else:
        specific_track[0][user_discord] = songs

# Função resposável por pegar músicas das lista top-músicas
def get_top_musics(user_discord:str):
    return top_tracks[0][user_discord]

# Função resposável por pegar músicas das lista de músicas recomendadas
def get_recomendations_musics(user_discord:str):
    return recomendations_tracks[0][user_discord]

# Função resposável por pegar músicas das lista do comando play
def get_track(user_discord:str):
    return specific_track[0][user_discord]
