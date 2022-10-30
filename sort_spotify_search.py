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
    for result in sorted_results[:args.n]:
        print(f"{result['name'][:30]:<30}\t{likes[result['id']]:<10}\t{result['external_urls']['spotify']:>}")


if __name__ == "__main__":
    main()
