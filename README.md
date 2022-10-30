<div align="center">

# Better Spotify Search

Sort your Spotify Searches

</div>

---

## Why 🤔

The inbuilt Spotify search functionality does not allow to sort by likes/followers. The default sorting does not make
sense (maybe a combination of hotness, recommendation, and popularity) which I dislike.

## How 🧐

Just used [Spotipy](https://spotipy.readthedocs.io/)'s API.

## Usage 👨‍💻

Getting API Keys: 
- Create an app on https://developers.spotify.com/. Add your new ID and SECRET to your environment:

Contributing: 
- Use ```pip install -r requirements.txt``` to install the requirements.
- Go through Spotipy's [docs](https://github.com/plamere/spotipy#installation) for reading about the functionalities.
That's it!

```shell
python sort_spotify_search.py -q SEARCH_QUERY [-n NUMBER_OF_RESULTS]
```
