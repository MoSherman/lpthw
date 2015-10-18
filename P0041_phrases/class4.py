#more class practice
#START 

#importing exit module
from sys import exit

#naming class
class Journey(object):
    
    #instating class with an object of position
    def __init__(self, side):
        self.side = side
    
    #whatever choice is made for var1 will be the instance
    def choice_1(self):
        
        if self.side == 'light':
            print "You went towards the light."
            light_side()
        
        elif self.side == 'dark':
            print "You went towards the dark."
            dark_side()
        
        else:
            print "You couldn't choose a side and you died in the battle."
            exit(0)
     
     def light_side():
        
        print "You choose the light side, you won the battle!"
        exit(0)
     
     def dark_side():
        
        print "You choose the dark side, you lost the battle!"
        print "But don't worry, you will probably come back in the next movie!"
        exit(0)

var1 = raw_input("What side will you choose for the battle? Light or Dark?" )

game1 = Journey(var1)

game1.choice_1()
        
    


#END
