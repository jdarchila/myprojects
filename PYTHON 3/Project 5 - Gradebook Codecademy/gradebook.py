last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics", "calculus", "poetry", "history"]

grades = ["98", "97", "85", "88"]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print("")

print(gradebook)

gradebook.append (["computer science", 100])

print(gradebook)

print("")

gradebook.append (["visual arts", 93])

print(gradebook)

print("")

gradebook [-1][-1] = 93+5

print(gradebook)

print("")

gradebook[2].remove(85)

print(gradebook)

print("")

gradebook[2].append("Pass")

print(gradebook)

print("")

full_gradebook = last_semester_gradebook + gradebook 

print(full_gradebook)