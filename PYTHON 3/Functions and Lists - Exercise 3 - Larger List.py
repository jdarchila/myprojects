#Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt.

#In our code, we can represent the id of the items using numbers and conveyor belts using lists. For instance, if we have two lists, [23, 12, 21] and [1, 23], representing the id of the items at two conveyor belts, the output will be 21. Similarly, for input lists [1, 7, 2, 3, 17] and [1, 23, 24, 47, 71, 83], the output will be 83. For input lists [23, 12, 21] and [1, 23, 25], the output will be 21 as both lists are of the same length.

#Here are the steps you need to complete this code challenge:

#1. Define a function that accepts two parameters for our two lists of numbers.
#2. Check if the length of the first list is greater than or equal to the length of the second list.
#3. If true, then return the last element from the first list. Otherwise, return the last element from the second list.

#Write a function named larger_list() that has two parameters named my_list1 and my_list2.

#The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.

def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]
  
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

