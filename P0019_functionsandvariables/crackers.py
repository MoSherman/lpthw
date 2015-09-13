#Based on exercise 19 of lpthw

#START


#crackers function
def crackers(a_crackers, b_crackers):
    print "There are %d crackers of the type a." % a_crackers
    print "There are %d crackers of the type b." % b_crackers
    print "There are %d crackers in total." % (a_crackers + b_crackers)
    print "That's a lot of crackers.\n"


#first run
print "This time I am going to simply tell it how many crackers there are."
crackers(10, 10) 

raw_input("Coninue to run 2 of crackers function?\n")

#second run
print "This time we are going to use math in the function arg."
crackers (4 + 3, 5 + 7) 

raw_input("Coninue to run 3 of crackers function?\n")

#third run 
print "This time we are going to use variables."
a_amount = 17
b_amount = 23 

crackers(a_amount, b_amount) 

raw_input("Coninue to run 4 of crackers function?\n")

#fourth run 
print "This time we are going to use our variables from above and math."
crackers (a_amount + 30, b_amount + 30) 

raw_input("Coninue to run 5 of crackers function?\n")

#fifth run
print "This time we are going to ask for user input in the termial"
a_amount2 = raw_input("Amount of a type crackers? ")
a_entered = int(a_amount2) 
b_amount2 = raw_input("Amount of b type crackers? ")
b_entered = int(b_amount2) 

crackers(a_entered, b_entered)

raw_input("Coninue to run 6 of crackers function?\n")

#sixth run
print "This time we are going to use user input and math to add 20."
a_amount3 = raw_input("Amount of a type crackers? ")
a_entered3 = int(a_amount3)
b_amount3 = raw_input("Amount of b type crackers? ")
b_entered3 = int(b_amount3)

crackers(a_entered3 + 20, b_entered3 + 20)

raw_input("Coninue to run 7 of crackers function?\n")

#seventh run
print "This time I'm going to try and use argv."
from sys import argv 
script, a_argv, b_argv = argv
a_input = int(a_argv)
b_input = int(b_argv)

crackers(a_input, b_input) 


raw_input("Coninue to run 8 of crackers function?\n")

#eighth run
print "This time I'm going to try and combine a lot of different things."
a_raw = raw_input("How many more type a crackers do you have? ")
a_var = float(a_raw)
b_raw = raw_input("How many more type b crackers do you have? ")
b_var = float(b_raw)

crackers (a_input + 20 + a_var, b_input + 20 + b_var)



#END
