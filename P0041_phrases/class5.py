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
    
        def light_side():
        
            print "You choose the light side, you won the battle!"
            exit(0)
     
        def dark_side():
        
            print "You choose the dark side, you lost the battle!"
            print "But don't worry, you can still win!"
            choice = raw_input("Will you throw over you dark ways? ")
            
            if choice == 'yes':
                light_side()
            
            elif choice == 'no':
                print "Well then your def dead!"
                exit(0)
            
            else:
                print "You couldn't choose and you died in prison."            
                exit(0)
        
        if self.side == 'light':
            print "You went towards the light."
            light_side()
        
        elif self.side == 'dark':
            print "You went towards the dark."
            dark_side()
        
        else:
            print "You couldn't choose a side and you died in the battle."
            exit(0)
        

var1 = raw_input("What side will you choose for the battle? Light or Dark?" )

game1 = Journey(var1)

game1.choice_1()
        
    


#END
