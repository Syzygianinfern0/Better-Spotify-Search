from argparse import ArgumentParser

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

ID = None
SECRET = None


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-q", help="Query")
    parser.add_argument("-n", default=20, help="Number of results to display")
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=ID,
            client_secret=SECRET,
        ),
    )

    results = sp.search(args.q, 50, type="playlist")["playlists"]["items"]
    likes = {playlist["id"]: sp.playlist(playlist["id"])["followers"]["total"] for playlist in results}
    sorted_results = sorted(results, key=lambda playlist: likes[playlist["id"]], reverse=True)
    for n in range(0, int(args.n)):
        print(f"{sorted_results[n]['name'][:30]:<30}\t{likes[sorted_results[n]['id']]:<10}\t{sorted_results[n]['external_urls']['spotify']:>}")


if __name__ == "__main__":
    main()
