#For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder. In order to do this we will need to:

#Define the function to accept two parameters
#Multiply the first input value by 2
#Divide the second input value by 2
#Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
#Return the answer

#Write a function named remainder() that has two parameters named num1 and num2.

#The function should return the remainder of twice num1 divided by half of num2.

def remainder(num1, num2):
  return ((num1*2)%(num2/2))

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0