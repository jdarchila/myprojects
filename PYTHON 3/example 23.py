#4. Twice As Large
#In this challenge, we will determine if one number is twice as large as another number. To do this, we will compare the first number with two times the second number. Here are the steps:

#Define our function with two inputs num1 and num2
#Multiply the second input by 2
#Use an if statement to compare the result of the last calculation with the first input
#If num1 is greater then return True otherwise return False


def twice_as_large(num1, num2):
  if num1 >= num2 *2:
    return True
  else:
    return False
#Example
print(twice_as_large(1, 3)) # True 