from config import Album, Artist, NAME_PATTERN, COUNTING_PATTERN
import re


def read_file(filename):
    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            result.append(line)

    return result


def parse_artist(artist_info):

    if ' - [' in artist_info:
        lines = artist_info.split('\n')

        name = re.match(NAME_PATTERN, lines[0]).group(1)
        counter = ''
        for c in lines[0]:
            if c == '[':
                counter += c
            elif counter and not counter.endswith(']'):
                counter += c

        listened, total = counter[1:len(counter)-1].split('/')
        discography = []
        for i in range(1, len(lines)):
            parts = lines[i].split('.')
            if len(parts) >= 2:
                discography.append(Album(parts[1].lstrip(), int(parts[0].replace('\t', ''))))

        return Artist(name, sorted(discography), int(listened), int(total))

    else:
        artist_info = (artist_info.replace('\n', '').rstrip()) + ' -'
        name = re.match(NAME_PATTERN, artist_info).group(1)
        return Artist(name, [], 0, 0)


def get_artists(filename):

    file = read_file(filename)
    artists = []
    artist_info = ''
    for line in file:
        if line.startswith('*'):
            if artist_info != '':
                artists.append(parse_artist(artist_info))
            artist_info = line
        else:
            artist_info += line
    artists.append(parse_artist(artist_info))

    artists = list(filter(lambda x: (not x.already_listened()), artists))

    return sorted(artists)

