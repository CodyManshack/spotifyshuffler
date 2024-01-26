<h1 align="center">Spotify Shuffler</h1>

This is a simple script meant to be ran on a cron to automatically shuffle your Spotify playlists.
The only dependency is Spotipy.

# Usage
Unfortunately, this script must first be ran manually before it can be put on a cron because it requires OAuth permissions. This authentication method will cache in the directory in the `.cache` directory and will be usable for some amount of time.

This script also requires a Spotify developer account to be created that is attached to your Spotify account, so that you can get a Spotify Client ID & Secret to use in the requests.

## Setup
1. Create your Spotify developer account and retrieve the client_id and secret. https://developer.spotify.com/

2. Create a `.env` file in the source directory that contains the following keys:

    * SPOTIPY_CLIENT_ID=uuid
    * SPOTIPY_CLIENT_SECRET=uuid
    * SPOTIPY_REDIRECT_URI=http://localhost:9091/callback
    * SHUFFLE_PLAYLIST_IDS='["uuid", "uuid"]'

# Run
Simply run this script like any other Pyton script: `python shuffler.py` and it will execute :)

## Windows Cron
I included a `.bat` file that will run this file properly within its Python `venv` on your local machine. This is useful for setting up automatic execution as a task in Windows Task Scheduler.
> Remember that this must be executed manually first!!