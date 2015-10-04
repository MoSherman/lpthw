#Converting to a function 

#START 

i_define = raw_input("What is i? ") 
i = int(i_define)
numbers = []

def while_loop(i): 
    while i < 10: 
        print "At the top i is %d" %i
        numbers.append(i)
        
        i = i + 1
        print "Numbers now: ", numbers 
        print "At the bottom i is %d" % i
    
    print "The numbers: "
    
    for num in numbers: 
        print num

while_loop(i)

raw_input("Run next loop with i + 2 in function arg line? Hit Enter.")

while_loop(i + 2)

#END

