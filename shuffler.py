import logging
import os
import random
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


def main():
    log = logging.getLogger('shuffler')
    logFormatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s %(message)s')
    logHandler = logging.FileHandler(filename='shuffler.log', mode='a')
    logHandler.setFormatter(logFormatter)
    log.addHandler(logHandler)
    log.setLevel(logging.DEBUG)
    load_dotenv()
    scope = "playlist-modify-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative"
    spotify = Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlist_ids = [p for p in os.getenv("SHUFFLE_PLAYLIST_IDS").split(",")]
    for playlist_id in playlist_ids:
        playlist = spotify.playlist(playlist_id, fields="name,tracks")
        playlist_length = playlist["tracks"]["total"]
        log.info(f'shuffling: {playlist["name"]} with {playlist_length} tracks')
        r = [ random.randrange(playlist_length - 1) for i in range(playlist_length)]
        log.debug(f'generated random list: {r}')
        for i in range(playlist_length):
            result = spotify.playlist_reorder_items(playlist_id, range_start=i, range_length=1, insert_before=r[i])
            log.debug(f'playlist: {playlist["name"]} position: {i} new position: {r[i]}')

if __name__ == "__main__":
    main()