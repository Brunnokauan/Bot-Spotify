import discord
from commands import *
from access import authorization
import songs

class ButtonsTopSongs(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Tocar Música", style=discord.ButtonStyle.primary, emoji="🎵")
    async def toca_musica(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        s = songs.get_top_musics(user)
        await interaction.response.send_message(listen_songs(token, s), ephemeral=True) # Send a message when the button is clicked

    @discord.ui.button(label="Pausar Música", style=discord.ButtonStyle.danger)
    async def pausa_musica(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        await interaction.response.send_message(pause_songs(token), ephemeral=True)

    # @discord.ui.button(label="Modo Aleatório", style=discord.ButtonStyle.primary)
    # async def button_callback(self, button, interaction: discord.Interaction):
    #     await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

class ButtonsRecomendationsSongs(discord.ui.View):
    @discord.ui.button(label="Tocar Música", style=discord.ButtonStyle.primary, emoji="🎵")
    async def toca_musica(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        s = songs.get_recomendations_musics(user)
        await interaction.response.send_message(listen_songs(token, s), ephemeral=True)

    @discord.ui.button(label="Pausar Música", style=discord.ButtonStyle.danger)
    async def pausa_musica(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        await interaction.response.send_message(pause_songs(token), ephemeral=True)

    # @discord.ui.button(label="Modo Aleatório", style=discord.ButtonStyle.primary)
    # async def button_callback(self, button, interaction: discord.Interaction):
    #     await interaction.response.send_message("You clicked the button!")

class ButtonsPlays(discord.ui.View):
    @discord.ui.button(label="Música 1", style=discord.ButtonStyle.success)
    async def m1(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        s = songs.get_track(user)
        await interaction.response.send_message(listen_songs(token, [s[0]]), ephemeral=True) 

    @discord.ui.button(label="Música 2", style=discord.ButtonStyle.success)
    async def m2(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        s = songs.get_track(user)
        await interaction.response.send_message(listen_songs(token, [s[1]]), ephemeral=True)

    @discord.ui.button(label="Música 3", style=discord.ButtonStyle.success)
    async def m3(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        s = songs.get_track(user)
        await interaction.response.send_message(listen_songs(token, [s[2]]), ephemeral=True)
    
    @discord.ui.button(label="Música 4", style=discord.ButtonStyle.success)
    async def m4(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        s = songs.get_track(user)
        await interaction.response.send_message(listen_songs(token, [s[3]]), ephemeral=True)
    
    @discord.ui.button(label="Música 5", style=discord.ButtonStyle.success)
    async def m5(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        s = songs.get_track(user)
        await interaction.response.send_message(listen_songs(token, [s[4]]), ephemeral=True)
    
    @discord.ui.button(label="Pausar Música", style=discord.ButtonStyle.danger)
    async def pausa_musica(self, interaction: discord.Interaction, button):
        user = interaction.user.display_name
        token = authorization(user)
        await interaction.response.send_message(pause_songs(token), ephemeral=True)
        