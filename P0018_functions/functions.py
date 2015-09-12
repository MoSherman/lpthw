#This is based on exercise 18 of lpthw

#START 

#this one is like your scripts with argv 
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
#the *argv is not needed here is a simplier way 
def print_two_again(arg1, arg2): 
    print "arg1: %r, arg2: %r" % (arg1, arg2) 
    
# function with one arguement 
def print_one(arg1): 
    print "arg1: %r" % arg1
    
# no arguements 

def none():
    print "I've got nothing."


print_two("Mo", "Sherman")
print_two_again("Mo", "Sherman")
print_one("First")
print_none()

#END
