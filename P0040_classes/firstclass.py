#Based on exercise 40 of lpthw 
#START 

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics 
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday to You!", 
                    "I don't want to get sued", 
                    "So I'll stop here."]) 

bulls_on_parade = Song(["More lines of a song", 
                        "That I don't know."])

happy_bday.sing_me_a_song()

print '_' * 10

bulls_on_parade.sing_me_a_song()

#END


                    
