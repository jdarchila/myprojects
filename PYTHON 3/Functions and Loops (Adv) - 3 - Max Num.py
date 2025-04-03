#Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

#Define the function to accept a list of numbers called nums
#Set our default maximum value to be the first element in the list
#Loop through every number in the list of numbers
#Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
#Return the maximum number

#Create a function named max_num() that takes a list of numbers named nums as a parameter.

#The function should return the largest number in nums

#One way  
def max_num(nums):
  max_value = [0]
  for num in nums:
    if num > max_value[0]:
      max_value[0]= num 
  return max_value 

print(max_num([50, -10, 0, 75, 20])) # 75


print("")

#Another way

def max_num2(nums2):
  for num2 in nums2:
    if num2 == max(nums2):
      return num2 
  return num2

print (max_num2([50, -10, 0, 75, 20])) # 75

print ("")

#Another way

def max_num3(nums3):
  maximum = nums3[0]
  for number in nums3:
    if number > maximum:
      maximum = number
  return maximum
  

print(max_num3([50, -10, 0, 75, 20])) # 75