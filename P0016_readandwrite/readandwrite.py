#Base don exercise 16 of learn python the hard way. 

#START 

from sys import argv 

script, filename = argv 

print "We're going to erase %r." % filename 
print "If you don't want that, hit CTRL-C (^c)."
print "If you do want that hit RETURN."

raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

#Removing truncate becasue I think it is implied in w mode
#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input('line 1: ')
line2 = raw_input('line 2: ') 
line3 = raw_input('line 3: ')

print "I'm going to write these to the file."

target.write("%r \n %r \n %r" % (line1, line2, line3) )

print "And finally, we close it."
target.close()

#END 
