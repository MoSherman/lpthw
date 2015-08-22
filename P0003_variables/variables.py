#P0003_variables is about learning how to define variables in a script and then use those variables in statements and equations 

# variables are defined be simplying typing the varaible followed by and = and defining what the variable is with either numbers or using previously defined variables in a written equation

#START 

cars = 100
space_in_a_car = 4.0
drivers = 30 
passengers = 90
cars_not_driven = cars - drivers 
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven 


print "There are", cars, "cars available."
print "There are only", drivers, "drivers avaible."
print "There will be", cars_not_driven, "empty cars today." 
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#END
