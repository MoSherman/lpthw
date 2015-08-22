#This is a practice file for defining variables.
#This is my second attempt at this same family program, now that I know how to embed variables into strings, it should look a lot better then the previou practice.py file 

#Start 

sister = 'Sarah'
mother = 'Caroline' 
father = 'Marc' 
user = 'Moriah' 
total_relatives_added = 3
female_sibilings = 1 
female_relatives = 2
male_sibilings = 0 
male_relatives = 1 
female_gender_possesive = 'her'


print "%s has added %d relatives" % (user, total_relatives_added)
print "%s has %d sister, %s name is %s." % (user, female_sibilings, female_gender_possesive, sister)
print "%s has %d brothers." % (user, male_sibilings)
print "%s's mother's name is %s." % (user, mother) 
print "%s's father's name is %s." % (user, father)

#END 
