#Based on lpthw exercise 10
#more exscape practice 

#START 

after_gym = 'Nandos'
otherwise = 'grilled cheese, eggs, pasta, something simple'

formatter = %s 

print ''' I have a lot of favorite foods \nbut after the gym
my favourit food is %r ''' % after_gym

print "Otherwise I just eat %s." % otherwise

print "But if I could I would eat", formatter, "all the time." % after_gym


#END
