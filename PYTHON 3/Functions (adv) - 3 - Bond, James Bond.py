#It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want. The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous phrase but replaced with our inputs. To accomplish this, we need to:

#Define the function to accept two parameters, first_name and last_name
#Concatenate the string ', ' on to the last_name
#Concatenate the first_name on to the result of the previous step
#Concatenate a space on to the result
#Concatenate the last_name again to the result
#Return the final string

#Write a function named introduction() that has two parameters named first_name and last_name.

#The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
