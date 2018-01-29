class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

last_mile_home = Song(["Dreaming on the last mile home",
                        "Things are always better",
                        "When we're all together",
                        "I'm dreaming on the last mile home"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

last_mile_home.sing_me_a_song()
