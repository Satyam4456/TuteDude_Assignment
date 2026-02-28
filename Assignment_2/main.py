## Tast - 1: Check if a Number is Even or Odd

number = int(input("\nEnter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


## Task - 2: Sum of Integers from 1 to 50 Using a Loop

total_sum = 0
i = 1
while i <= 50:
    total_sum += i
    i += 1
print(f"\nThe sum of integers from 1 to 50 is: {total_sum}\n")