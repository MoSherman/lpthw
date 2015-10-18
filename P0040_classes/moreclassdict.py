#my first attempt at simple classes 
#Who is this?
#START 

class Identify(object):

    def __init__(self, person):
        self.person = person 
         
    
    def person_id(self):
        for line in self.person:
            print line


name_1 = 'Moriah'
age_1 = 27

name_2 = 'Sarah'
age_2 = 28


person_1 = Identify([name_1 , age_1])

person_2 = Identify([name_2 , age_2])


person_1.person_id()

print ' ' * 10
print ' ' * 10

person_2.person_id()

#END
