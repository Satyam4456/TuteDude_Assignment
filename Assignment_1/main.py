## Task_1: Perform Basic Mathematical Operations

# Taking the input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

## performing basic math operations
sum = round(num1 + num2,2)
difference = round(num1 - num2,2)
product = round(num1 * num2,2)
division = (num1 / num2 if num2 != 0 else "undefined (division by zero)").__round__(2)

## getting the output
print()
print(f"Addition: %g" %(sum))
print(f"Subtraction: %g" %(difference))
print(f"Multiplication: %g" %(product))
print("Division: %g" %(division)) 


## Task_2: Create a Personalized Greeting

# getting the input from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# getting the output
print()
print(f"Hello, {first_name + " " + last_name}! Welcome to the Python program.")
