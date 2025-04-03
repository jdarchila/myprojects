#Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order to do this, we need to do a few steps:

#Define the function with two input parameters, num1 and num2
#Calculate the sum of the two numbers
#Divide the sum by the number of inputs to the function
#Return the answer

#Write a function named average() that has two parameters named num1 and num2.

#The function should return the average of these two numbers.

def average(num1, num2):
  return (num1 + num2) / 2 

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0