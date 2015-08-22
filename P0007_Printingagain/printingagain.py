#Based on exercise 8 of learn python the hardway 

#Start 

#Variable definition, must remember %r should be within quotes here
formatter = "%r %r %r %r" 

#display the data defined in paranth in place of %r
print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter,formatter, formatter)

#printing lots of strings together and good style
print formatter % (
    "I had this thing.", 
    "That you could type up right.", 
    "But it didn't sing.", 
    "So I said goodnight."
)

#END
