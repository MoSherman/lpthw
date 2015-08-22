#This is a practice file for defining variables.

#Start 

sister = "Sarah" 
mother = "Caroline" 
father = "Marc" 
user = "Moriah" 
total_relatives_added = 3
female_sibilings = 1 
female_relatives = 2
male_sibilings = 0 
male_relatives = 1 
gender_possesive = "her"


print user, "has added", total_relatives_added, "relatives."
print user, "has", female_sibilings, "sister named", sister, "."
print user, "has", female_relatives, "women in", gender_possesive, "family."
print user, "'s mother is named", mother, "." 
print user, "has", male_sibilings, "brothers."
print user, "has only", male_relatives, "male relative."
print user, "'s", male_relatives, "male relative is her father named", father, "."


#Not sure what % does her exactly but seems to allow varaible insertion into print statement without having to close the statement by defining after the statement which variable sould be inserted.
print 
print 
print "Hey %s there." % "you"
print "My name is %s." % "Moriah"
print "My name is %s." % user





#END
