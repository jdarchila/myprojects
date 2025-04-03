#Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. These are the steps we need to complete this:

#1. Define the function to accept one input parameter called nums
#2. Initialize a counter to 0
#3. Loop through every number in nums
#4. Within the loop, if any of the numbers are divisible by 10, increment our counter
#5. Return the final counter value

#Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

#Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
  count = 0 
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count 
    
print(divisible_by_ten([20, 25, 30, 35, 40]))

