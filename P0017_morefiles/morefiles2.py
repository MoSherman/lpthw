#This is based on exercise 17 of lpthw

#START 

from sys import argv 
from os.path import exists 

script, from_file, to_file = argv 

print "Copying from %s to %s" % (from_file, to_file) 

in_file = open(from_file)
indata = in_file.read() 

print "This input file is %d bytes long" % len(indata) 

print "Does the output file exist? %r" % exists(to_file)
print "Ready? Hit Return to continue." 
raw_input("?")

out_file = open(to_file, 'w')
out_file.write(indata) 

print "done"

out_file.close() 
in_file.close()

#END
