#Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. This function will accept both of those values as inputs and return the amount of money to tip. In order to do this, we will need a few steps:

#Define the function to accept the total cost of the food called total and the percentage to tip as percentage
#Calculate the tip amount by multiplying the total and percentage and dividing by 100
#Return the tip amount

#Create a function called tip() that has two parameters named total and percentage.

#This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
  return (total*percentage)/100

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0