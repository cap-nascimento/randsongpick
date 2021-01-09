from config import Album, Artist
from parse import get_artists
from util import binary_search
import random


def menu():
    print("1 - Add an artist;")
    print("2 - Add an album;")
    print("3 - Exit;")
    print("> ", end='')


def add_artist(artists):
    name = ''
    while True:
        name = input("Type the name of the artist: ")
        if binary_search(artists, Artist(name, [], 0, 0)) != -1:
            print("This artist is already on the list!")
        else:
            break

    artists.append(Artist(name, [], 0, 0))
    return sorted(artists)


def add_album(artists):

    print("Choosing a random artist...")
    artist_number = random.randint(1, len(artists))
    if artists[artist_number-1].total == 0:
        total = int(input(f"How many albums {artists[artist_number-1].name} has? "))
        artists[artist_number-1].total = total

    album_number = 0
    while True:
        album_number = random.randint(1, artists[artist_number-1].total)
        already = False
        for album in artists[artist_number-1].discography:
            if album.number == album_number:
                already = True
                break
        if not already:
            break
    print(f"Add the album number {album_number} from {artists[artist_number-1].name} in your playlist!")
    album_name = input("Name of the album: ")
    artists[artist_number - 1].discography.append(Album(album_name, album_number))
    artists[artist_number - 1].listened += 1

    artists[artist_number - 1].discography.sort()
    return artists


if __name__ == '__main__':
    artists = get_artists('artists.txt')
    menu()
    while True:
        option = input()
        if option == '1':
            artists = add_artist(artists)
        elif option == '2':
            artists = add_album(artists)
        elif option == '3':
            break
        else:
            print("Invalid option!")
        menu()

    output = open('artists.txt', 'w', encoding='utf-8')
    for artist in artists:
        output.write(str(artist))
    output.close()
