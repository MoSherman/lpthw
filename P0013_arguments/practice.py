#More practice for exercise 13.
#Trying to combine raw input with argv.

#START

from sys import argv 

script, name = argv

name = raw_input ("What is you name? ")

print "What script is this?", script 
print "Who wrote it?", name 
print "Did that actually work?"
print "It did work, yay!"

#END
