class Album:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'\t{self.number}. {self.name}\n'

    def __lt__(self, other):
        return self.number < other.number


class Artist:
    def __init__(self, name, discography, listened, total):
        self.name = name
        self.discography = discography
        self.listened = listened
        self.total = total

    def __str__(self):
        result = ''
        if self.listened != 0:
            result = f'* {self.name} - [{len(self.discography)}/{self.total}]\n\n'
            for album in self.discography:
                result += str(album)
            result += '\n'
        else:
            result = f'* {self.name}\n'

        return result

    def __lt__(self, other):
        return self.name < other.name

    def already_listened(self):
        return len(self.discography) == self.total and self.total != 0


NAME_PATTERN = r"\*\s(.*)\s\-"
COUNTING_PATTERN = r"\[(.*)\]"
