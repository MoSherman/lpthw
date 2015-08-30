#More practice trying same exercise with no arv to see why its not great.

#START 

filename = raw_input("What is your filename? ")

txt = open(filename)

print "Your filename is %r:" % filename
print txt.read()

print "Type your file name again:"
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()

#END
