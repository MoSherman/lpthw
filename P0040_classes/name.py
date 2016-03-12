""" 
A script to allow someone to enter their name.
"""

class Name(object):
    
    def __init__(self, names):
        self.names = names 
    
    def your_name(self):
        
        print user_name
    
    def last_name(self):
        
        if user_name == 'Moriah':
            print "I bet your full name is %s Sherman" % user_name
            print "And your a developer!"
        
        elif user_name == 'Sarah':
            print "I bet your full name is %s Sherman" % user_name
            print "And your a lawyer!"
        
        elif user_name == 'Marc':
            print "I bet your full name is %s Sherman" % user_name
            print "And you work in IT!"
        
        elif user_name == 'Caroline':
            print "I bet your full name is %s Sherman" % user_name
            print "And you are the president of the womens club!"
        
        else:
            print "I bet your full name is %s Sherman" % user_name
    

user_name = raw_input("Whats your name? > ") 

user = Name(["user_name"])

user.your_name()
user.last_name()

user_name = raw_input("Whats your name user2? > ")

user2 = Name(["user_name"])

user2.your_name()
user2.last_name()