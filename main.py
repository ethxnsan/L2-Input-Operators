'''
userName = input ("Enter your name: ")
#print("Hey " + userName) 

userGrade = input("What grade are you in? ")
print ("Hey " + userName + ", " + userGrade + " is a lame grade")

userYear = int(input ("What year were you born? "))
userAge = 2022 - userYear
print(str(userAge) + " is so young!")
'''

# Create your own Madlibs
# Have at least 5 inputs

name1 = input("Please give me a name: ")
verb1 = input("Please give me a verb that ends with ing: ")
location = input("Please give me a location: ")
name2 = input("Please give me another name: ")
bodypart = input("Please give me a body part: ")
verb2 = input("Please give me another verb that ends with the letter s : ")
adverb1= input("Please give me an adverb: ")
verb3 = input("Please give me another verb: ")
verb4 = input("Please give me another verb that ends with the letter s: ")


print (name1  + " is " + verb1 + " " + name2 + " in a " + location)
print (name2 + " uses their " + bodypart + " and " + verb2 + " " +  name1 )
print (name1 + " turns around " + adverb1 + " and " + verb3 + " " +name2)
print (name1 + " annihilates " + name2 + " and decapitates him ")
print ("until " + name2 + " wakes up from the dead and " + verb4 + name1 )