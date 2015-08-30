#More questions practice.

#START 

print "What is you name?",
name = raw_input ()
print "Why are you here?",
purpose = raw_input () 
print "What the secret password?",
password = raw_input () 

print """"%r says they are here %r and that the password is %r.  
    Should I let %r in? """ % (name, purpose, password, name)
print "Yes, let %r in." % (name)

#END
