import logging
import os
import random
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


def main():
    log = logging.getLogger('shuffler')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(name)s] %(levelname)s %(message)s')
    load_dotenv()
    scope = "playlist-modify-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative"
    spotify = Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlist_ids = [p for p in os.getenv("SHUFFLE_PLAYLIST_IDS").split(",")]
    for playlist_id in playlist_ids:
        playlist = spotify.playlist(playlist_id, fields="name,tracks")
        playlist_length = playlist["tracks"]["total"]
        log.info(f'shuffling: {playlist["name"]} with {playlist_length} tracks')
        snapshot_id = None
        for i in range(playlist_length):
            random_item = random.randrange(playlist_length - 1)
            random_position = random.randrange(playlist_length - 1)
            snapshot_id = spotify.playlist_reorder_items(playlist_id, range_start=random_item, range_length=1, insert_before=random_position, snapshot_id=snapshot_id)["snapshot_id"]

if __name__ == "__main__":
    main()