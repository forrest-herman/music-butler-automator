# import os

from parse_music_butler import add_music_butler_feed_to_playlist

# load environment variables
# from dotenv import load_dotenv
# load_dotenv()

MUSIC_BUTLER_URL = 'https://www.musicbutler.io/'


def main():
    add_music_butler_feed_to_playlist(MUSIC_BUTLER_URL)


if __name__ == '__main__':
    main()
