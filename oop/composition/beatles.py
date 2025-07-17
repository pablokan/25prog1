class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def play_instrument(self):
        return f'{self.name} is playing the {self.instrument}'

class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def play_music(self):
        return [member.play_instrument() for member in self.members]

if __name__ == "__main__":
    john = Musician('John', 'Guitar')
    paul = Musician('Paul', 'Bass')
    george = Musician('George', 'Guitar')
    ringo = Musician('Ringo', 'Drums')

    beatles = Band('The Beatles', [john, paul, george, ringo])
    for music in beatles.play_music():
        print(music)

        