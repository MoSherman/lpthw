#more functions practice

#START

from sys import argv
from os.path import exists 

script, testfile = argv 

print "Does the test file exist? %r" %exists(testfile)

text = open(testfile)
print "The contents of the file:"
print text.read()


print "Keep going?"
raw_input('?')

def function1(arg1, arg2):
    print "arg1 is: %r, arg2 is: %r" % (arg1, arg2)


function1("Mo", "Sherman")

#END
