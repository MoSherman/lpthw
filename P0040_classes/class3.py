#more class practic
#START 

#importing exit module
from sys import exit

#naming class
class Stand_Up(object):
    
    #instating class with an object of position
    def __init__(self, position):
        self.position = position
    
    
    def stand_or_sit(self):
        
        if self.position == 'standing':
            print "Good on you for standing up." 
            exit(0)
        
        elif self.position =='sitting':
            print "You need to stand up!"
            what = raw_input("Are you standing yet? ")
            
            if what == 'yes':
                print "Good on you for standing up." 
                exit(0)
            elif what == 'no':
                print "Fine see if I care."
                exit(0)
            else:
                print "It's a yes or no answer dummy."
                what = raw_input("Are you standing yet? ")
        
        else:
            exit(0)

var1 = raw_input("Are you standing or sitting? ")

game_1 = Stand_Up(var1)

game_1.stand_or_sit()

#END
            
            
        
         
        
