#For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list. Here is what you need to do:

#Define a function that has two input parameters for our lists
#Loop through every index in one of the lists from beginning to end
#Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return False
#If the loop ended successfully, then we know the lists are reversed and we can return True.

#Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

#The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

#For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    # Loop through each index in lst1
    for i in range(len(lst1)):
        # Compare the element in lst1 with the corresponding element in lst2
        if lst1[i] != lst2[len(lst2) - 1 - i]:
            return False

    # If all elements matched, return True
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))