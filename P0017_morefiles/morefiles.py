#Based on exercise 17 of learn python the hard way. 

#START 

from sys import argv 
from os.path import exists 

script, from_file, to_file = argv 

in_file = open(from_file);
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

print "Alright, all done." 

#END
