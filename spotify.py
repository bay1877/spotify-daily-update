import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import weather_song, date_song

# Modify to match your username, desired playlist name, and the city you live in
username = "username"
playlist_name = "Daily Update"
my_city = "New York NY"

scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_playlist_id(username, playlist_name):
    """
    Given a user and a playlist name, return the playlist Id 
    :param city: the username of the user
    :param playlist_name: the name of playlist
    :return: the playlist Id
    """
    playlist_id = ''
    playlists = sp.user_playlists(username, limit=30)
    for playlist in playlists['items']:  # iterate through playlists I follow
        if playlist['name'] == playlist_name:  # filter for newly created playlist
            playlist_id = playlist['id']
    return playlist_id

def get_artist(artist):
    """
    Get artist data for a given artist
    :param artist: the name of the artist
    :return: the dictionary of the artist data
    """
    return sp.search(artist, type='artist', limit=1)

def get_artist_uri(artist):
    """
    Get an artist's Spotify URI
    :param artist: the name of the artist
    :return: the Spotify URI of the artist
    """
    return get_artist(artist)['artists']['items'][0]['uri']

def get_song(song):
    """
    Get song data for a given song
    :param song: the name of the song
    :return: the dictionary of the song data
    """
    return sp.search(song, type="track")

def get_song_uri(song):
    """
    Get an song's Spotify URI
    :param song: the name of the song
    :return: the Spotify URI of the song
    """
    return get_song(song)['tracks']['items'][0]['uri']

def get_podcast(podcast):
    """
    Get podcast data for a given podcast
    :param podcast: the name of the podcast
    :return: the dictionary of the podcast data
    """
    return sp.search(podcast, type="episode")

def get_podcast_uri(podcast):
    """
    Get an podcast's Spotify URI
    :param podcast: the name of the podcast
    :return: the Spotify URI of the podcast
    """
    return get_podcast(podcast)['episodes']['items'][0]['uri']

def get_show(show):
    """
    Get show data for a given show
    :param show: the name of the show
    :return: the dictionary of the show data
    """
    return sp.search(show, type="show")

def get_show_uri(show):
    """
    Get an show's Spotify URI
    :param show: the name of the show
    :return: the Spotify URI of the show
    """
    return get_show(show)['shows']['items'][0]['uri']

def get_newest_podcast_episode_uri(show):
    """
    Get the Spotify URI of a show's most recent podcast
    :param show: the name of the show
    :return: the Spotify URI of the show's most recent podcast
    """
    return sp.show_episodes(get_show_uri(show))["items"][0]["uri"]

def add_sky_song():
    """
    Get the sky info song and add it to the playlist
    :return:
    """
    playlist_id = get_playlist_id(username, playlist_name)
    tracks = list()
    tracks.append(get_song_uri(weather_song.get_sky_song(my_city)))
    sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)

def add_temperature_song():
    """
    Get the temperature song and add it to the playlist
    :return:
    """
    playlist_id = get_playlist_id(username, playlist_name)
    tracks = list()
    tracks.append(get_song_uri(weather_song.get_temperature_song(my_city)))
    sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)

def add_day_of_week_song():
    """
    Get the day of the week song and add it to the playlist
    :return:
    """
    playlist_id = get_playlist_id(username, playlist_name)
    tracks = list()
    tracks.append(get_song_uri(date_song.get_weekday_song()))
    sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)

def add_day_of_month_song():
    """
    Get the day of the month song and add it to the playlist
    :return:
    """
    playlist_id = get_playlist_id(username, playlist_name)
    tracks = list()
    day = date_song.get_monthday_song()
    if (day):
        tracks.append(get_song_uri(day))
        sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)

def add_podcast(show):
    """
    Get the most recent podcast from a show and add it to the playlist
    :return:
    """
    playlist_id = get_playlist_id(username, playlist_name)
    tracks = list()
    tracks.append(get_newest_podcast_episode_uri(show))
    sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)

def test_songs():
    """
    test that a string works to locate a song(s)
    :return:
    """
    playlist_id = get_playlist_id(username, playlist_name)
    tracks = list()
    tracks.append(get_song_uri("In The Air Tonight"))
    # tracks.append(get_song_uri(""))

    print(tracks)

    sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)

if __name__ == "__main__":
    # if the playlist exists already, delete it
    if(get_playlist_id(username, playlist_name)):
        print(f"Deleting playlist: {playlist_name}")
        sp.user_playlist_unfollow(username, get_playlist_id(username, playlist_name))

    print(f"Creating playlist: {playlist_name}")
    sp.user_playlist_create(username, playlist_name, public=True, collaborative=False, description='')

    # test_songs()
    add_day_of_week_song()
    add_day_of_month_song()
    add_sky_song()
    add_temperature_song()
    #add any daily podcast's
    add_podcast("The Bible Recap")
