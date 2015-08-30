#This is based on exercise 12 of learn python the hardway.

#START 

age = raw_input ("How old are you? ") 
height = raw_input ("How tall are you? ") 
weight = raw_input ("How much do you weight? ")


#Making height a string variable to see if that eliminates need for escape.
print "So you are %r years old, %s tall and %r heavy." % (
    age, height, weight)
    
#END
