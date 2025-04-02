numbers = [1,2,4,5,6,42,5,6,7,8,2,3,4,5,1,22,1,2,3,1,3,7,5]

lowest_number = min(numbers) #Gives the lowest number, no duplicates

print(lowest_number) 

print("--------------------------------------------") 

for number in numbers:
    if number == lowest_number:
      	print(number)
        

print("--------------------------------------------") 


repeated = numbers.count(lowest_number)

print(repeated)
        
   


  