from argparse import ArgumentParser
from tabulate import tabulate

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

    results = sp.search(args.q, args.n, type="playlist")["playlists"]["items"]
    likes = {playlist["id"]: sp.playlist(playlist["id"])["followers"]["total"] for playlist in results}
    sorted_results = sorted(results, key=lambda playlist: likes[playlist["id"]], reverse=True)
    sorted_table = []

    sorted_table.append(['Title', 'Likes', 'URL'])

    for result in sorted_results:
        row_list = []
        row_list.append(result['name'])
        row_list.append(likes[result['id']])
        row_list.append(result['external_urls']['spotify'])
        sorted_table.append(row_list)
    
    print(tabulate(sorted_table, headers='firstrow', tablefmt='fancy_grid'))


if __name__ == "__main__":
    main()
