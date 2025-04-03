#Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number. For this, we are going to need a few steps:

#Define the function header to accept one input parameter called num
#Print out 1 times num
#Print out 2 times num
#Print out 3 times num
#Return the value of 3 times num

#write a function named first_three_multiples() that has one parameter named num.

#This function should print the first three multiples of num. Then, it should return the third multiple.

#For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

print("")

#Another way

def first_three_multiples2(num2):
  print(num2)
  print(num2*2)
  print(num2*3)
  return num2*3

print(first_three_multiples2(10))
# should print 10, 20, 30, and return 30
print(first_three_multiples2(0))
# should print 0, 0, 0, and return 0
