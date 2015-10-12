#Based on exercise 36 of lpthw. 
#My first attempt at a text game.
#FIND SPOCK

#START

from sys import exit

def sick_bay():
    print "You have now entered sickbay, Dr. McCoy is here."
    print "You can ask him if he knows where Mr. Spock is or you can look around."
    
    choice = raw_input("> ")
    
    while choice != "ask" or choice != "look":
    
        if choice == "ask": 
            print "You asked Dr. McCoy, but he is a Doctor not a Detetective."
            print "He throws you out of sickbay."
            explode()
    
        elif choice == "look":
            print "You looked around, but Mr.Spock wasn't there."
            print "You decide to go look in the mess hall instead."
            mess_hall()
    
        else: 
            print "You can 'ask' or 'look'."
            choice = raw_input("> ")

def mess_hall():
    print "You have walked in to the mess hall."
    print "Mr. Scotty is here eating which makes you hungry."
    print "Do you ask Scotty where Mr. Spock is or get food?"
    
    choice = raw_input("> ")
    
    while choice != "ask" or choice != "get food":
        
        if choice == "ask":
            print "You asked Scotty where Mr. Spock is."
            print "He tells you Mr. Spock is meditating in his quaters."
        
            go = raw_input("Do you go to Mr. Spocks quaters? Y/N ")
            
            while go != "yes" or go != "no":
            
                if go == "yes":
                    quarters()
        
                elif go == "no":
                    explode()
        
                else:
                    print "It's a yes or no question."
                    go = raw_input("Do you go to Mr. Spocks quaters? Y/N ")
                    
        elif choice == "get food":
            print "You let your stomach over-rule your good sense." 
            explode()
        
        else:
            print "You can 'ask' or 'get food'."
            choice = raw_input("> ")
        
def quaters():
    print "You have finally made it to Mr. Spocks quaters."
    
    choice = raw_input("Do you knock or open the door? ")
    
    while choice != "knock" or choice != "open":
    
        if choice == "knock":
            print "Mr. Spock opens the door."
            congrats()
    
        elif choice == "open":
            print "Mr. Spock is annoyed by your actions and nerve pinches you."
            explode()
    
        else:
            print "Your choices are to 'knock' or 'open'."
            choice = raw_input("Do you knock or open the door? ")

def explode():
    print "You failed in your mission to get the code from Mr. Spock."
    print "Because of your poor choices the Enterprise explodes."
    print "Good job Ensign!"
    exit(0)

def congrats():
    print "Congratulations Ensign, you found Mr. Spock!"
    print "Mr. Spock told you the code and now the Enterprise will not explode!"
    print "Good job Ensign!"
    exit(0)

def start():
    print "You are an Ensign on the starship Enterprise."
    print "The ship decides to go into self-destruct mode your first day on the bridge."
    print "The captain can not stop it because he forgot the code."
    print "The captain sends you to find Mr. Spock who will know the code."
    print "You think Mr. Spock may be in sick bay or the mess hall."
    
    choice = raw_input("Where do you look first? ")
    
    if choice == "sick bay":
        sick_bay()
    
    elif choice == "mess hall":
        mess_hall()
    
    else:
        print "You couldn't choose where to look."
        explode()

start()

#END
    
