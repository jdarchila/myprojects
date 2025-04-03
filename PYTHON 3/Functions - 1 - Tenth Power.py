#Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. In order to do this we need to do three things:

#Set up the function header for tenth_power which accepts one parameter
#Take the tenth power of the input value
#Return the result

#Write a function named tenth_power() that has one parameter named num.

#The function should return num raised to the 10th power.

def tenth_power(num):
  return num ** 10

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024