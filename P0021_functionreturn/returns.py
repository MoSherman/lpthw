#Based on exercise 21 of lpthw.

#START

def add(a, b): 
    print "ADDING %d + %d" % (a, b)
    return a + b 

def subtract(a, b): 
    print "SUBTRACTING %d -%d" % (a, b)
    return a - b 

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b 
    
def divide(a, b):
    print "DIVIDE %d / %d" % (a, b) 
    return a / b 


print "\nLets do some math with just functions!"

age = add(20, 6)
height = subtract(170, 7)
weight = multiply(30, 2)
iq = divide(300, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d." % (age, height, weight, iq)

#A puzzle for extra credit 
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: %r. Can you do it by hand?" % what 

#END



