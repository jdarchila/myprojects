num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

#Create a variable called total_exercises and set it equal to 0.

total_exercises = 0 
total_exercises2 = 0 
total_exercises3 = ""

#Iterate through the values in the num_exercises dictionary and add each value to the total_exercises variable.

for i in num_exercises:
  total_exercises += num_exercises[i]

print(total_exercises)

print("")

#another way 
for value in num_exercises.values():
  total_exercises2 += value

print(total_exercises2)

print("")

#another way 

for key in num_exercises:
  total_exercises3 += key

print(total_exercises3)






