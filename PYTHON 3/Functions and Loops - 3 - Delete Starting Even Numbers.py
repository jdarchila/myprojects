#Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

#1. Define our function to accept a single input parameter my_list which is a list of numbers
#2. Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
#3. Within the loop, if the first number in the list is even, then remove the first number of the list
#4. Once we hit an odd number or we run out of numbers, return the modified list

#Write a function called delete_starting_evens() that has a parameter named my_list.

#The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.

#For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

#Make sure your function works even if every element in the list is even!

def delete_starting_evens(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0:
    my_list.pop(0)
  return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))