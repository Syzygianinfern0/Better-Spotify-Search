from argparse import ArgumentParser

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tabulate import tabulate

ID = None
SECRET = None


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-q", help="Query")
    parser.add_argument("-n", default=20, type=int, help="Number of results to display")
    parser.add_argument("--fetch", default=50, type=int)
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

    results = sp.search(args.q, args.fetch, type="playlist")["playlists"]["items"]
    likes = {playlist["id"]: sp.playlist(playlist["id"])["followers"]["total"] for playlist in results}
    sorted_results = sorted(results, key=lambda playlist: likes[playlist["id"]], reverse=True)
    sorted_table = [['Title', 'Likes', 'URL']]

    for result in sorted_results[:args.n]:
        row_list = [result['name'], likes[result['id']], result['external_urls']['spotify']]
        sorted_table.append(row_list)

    print(tabulate(sorted_table, headers='firstrow', tablefmt='fancy_grid'))


if __name__ == "__main__":
    main()
