#This is taken from exercise 5 of learn python the hardway


my_name = 'Mo Sherman'
my_age = 26 #for now...
my_height = 64 #inches
my_weight = 135 #pounds
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height 
print "She's %d pounds heavy." % my_weight #ok I think this means that % followed by s is for text values and followed by d for numbers?
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair) #so to insert more the one varaible simply insert  % and after string insert % and define order of embeding within parenth
print "Her teeth are usually %s depending on whotsit consumption." % my_teeth 

#next line is difficult 
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight) #so you can also put equations in the parant to insert a variable after it has calculated.

#END
