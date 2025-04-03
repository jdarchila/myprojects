#We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this, we will need the following steps:

#Define the function to accept a list of numbers
#Create a variable to keep track of our sum
#Iterate through every element in our list of numbers
#Within the loop, add the current number we are looking at to our sum
#Still within the loop, check if the sum is greater than 9000. If it is, end the loop
#Return the value of the sum when we ended our loop

#Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

#The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

#For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

def over_nine_thousand (lst):
  total = 0 
  for num in lst:
    total += num
    if total > 9000:
      break 
  return total 
    
print(over_nine_thousand([8000, 900, 120, 5000]))    




    
  