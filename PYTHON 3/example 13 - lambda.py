numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) 

print(squared) 


cubes = list (map(lambda x: x ** 3, numbers))

print(cubes)

print("")

others = list(map(lambda x: x*2, numbers))

print(others)

print("")

others = list(map(lambda x: x*3, numbers))

print(others)