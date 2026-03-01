# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Mohammed Parkar 
# Date:

print("--- Factorial Finder ---\n")


# Write your code here
num = int(input("Enter a number: "))

fact = 1

# Checking if number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)
