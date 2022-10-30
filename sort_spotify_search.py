import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id="",
        client_secret="",
    ),
)

results = sp.search("lofi", 20, type="playlist")["playlists"]["items"]
likes = {playlist["id"]: sp.playlist(playlist["id"])["followers"]["total"] for playlist in results}
sorted_results = sorted(results, key=lambda playlist: likes[playlist["id"]], reverse=True)
for result in sorted_results:
    print(f"{result['name'][:30]:<30}\t{likes[result['id']]:<10}\t{result['external_urls']['spotify']:>}")
