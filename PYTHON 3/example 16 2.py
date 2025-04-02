
def get_valid_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Invalid input. Please enter a numeric value.")

num1 = get_valid_number("Enter a number: ")
num2 = get_valid_number("Enter another number: ")
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}.")
   
