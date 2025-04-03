# We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

#1. Define the function to accept two input parameters: lst1 and lst2
#2. Create two variables to record the two sums
#3. Loop through the first list and add up all of the numbers
#4. Loop through the second list and add up all of the numbers
#5. Compare the first and second sum and return the list with the greater sum

#Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

#The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
  sum1 = 0 
  sum2 = 0 
  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num 

  if sum1 >= sum2:
    return lst1
  elif sum2 > sum1:
    return lst2
  
print(larger_sum([1, 9, 5], [2, 3, 7]))