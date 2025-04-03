#Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age. This will require a few steps:

#Define the function called dog_years to accept two parameters: name and age
#Calculate the age of the dog in dog years
#Concatenate the string with the dog’s name and age in dog years
#Return the resulting string

#Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

def dog_years(name, age):
  return name + " is " + str((age *7)) + " years old in dog years." 

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

