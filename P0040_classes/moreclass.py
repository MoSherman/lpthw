#my first attempt at simple classes 
#Who is this?
#START 

class Identify(object):

    def __init__(self, person):
        self.person = person 
         
    
    def person_id(self):
        for line in self.person:
            print line

moriah = Identify(['Moriah', 27])

sarah = Identify(['Sarah', 28])


moriah.person_id()

print ' ' * 10
print ' ' * 10

sarah.person_id()

#END
        
