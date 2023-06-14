import pandas as pd
import streamlit as st

from sort_spotify_search import sort_spotify_search


def make_clickable(link):
    return f'<a target="_blank" href="{link}">🔗</a>'


def main():
    st.title("Spotify Playlist Search")

    # Input text field
    input_text = st.text_input("Playlist query")

    # Process input and display table
    if st.button("Search"):
        table_data = sort_spotify_search(input_text)
        table = pd.DataFrame(table_data[1:], columns=table_data[0])
        table["URL"] = table["URL"].apply(make_clickable)

        st.write(table.to_html(escape=False, index=False), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
