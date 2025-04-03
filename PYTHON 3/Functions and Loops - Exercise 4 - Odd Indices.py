#This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. Here are the steps needed:

#1. Define the function header to accept one input which will be our list of numbers
#2. Create a new list which will hold our values to return
#3. Iterate through every odd index until the end of the list
#4. Within the loop, get the element at the current odd index and append it to our new list
#5. Return the list of elements which we got from the odd indices.

#Create a function named odd_indices() that has one parameter named my_list.

#The function should create a new empty list and add every element from my_list that has an odd index. The function should then return this new list.

#For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

def odd_indices(my_list):
    # Create a new empty list
    odd_indexed_elements = []
    
    # Iterate through the list using range to get odd indices
    for i in range(1, len(my_list), 2):
        # Append the element at the current odd index to the new list
        odd_indexed_elements.append(my_list[i])
    
    # Return the new list with elements at odd indices
    return odd_indexed_elements

print(odd_indices([4, 3, 7, 10, 11, -2]))

