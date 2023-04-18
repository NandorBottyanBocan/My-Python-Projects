# The input() function

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# The result of the input() function

ask = float(input("Enter a number: "))
something = ask ** 2.0
print(ask, "to the power of 2 is", something)

# More about input() and type casting

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# String operators

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# LAB - Simple input and output

# Scenario

# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.

# The results have to be printed to the console.

# You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.

# Test your code ‒ does it produce the results you expect?

# We won't show you any test data ‒ that would be too simple.

a = float(input("Enter first value: ")) # input a float value for variable a here
b = float(input("Enter second value: ")) # input a float value for variable b here

print("Addition:", a + b) # output the result of addition here
print("Subtraction:", a - b) # output the result of subtraction here
print("Multiplication:", a * b) # output the result of multiplication here
print("Division:", a / b) # output the result of division here

print("\nThat's all, folks!")

# LAB - Operators and expressions

# Scenario

# Your task is to complete the code in order to evaluate the following expression:

# The result should be assigned to y. Be careful ‒ watch the operators and keep their priorities in mind.
# Don't hesitate to use as many parentheses as you need.

# You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.

# Test Data

# Sample input: 1
# Expected output: y = 0.6000000000000001

# Sample input: 10
# Expected output: y = 0.09901951266867294

# Sample input: 100
# Expected output: y = 0.009999000199950014

# Sample input: -5
# Expected output: y = -0.19258202567760344

x = float(input("Enter value for x: "))

y = 1./(x + 1./(x + 1./(x + 1./x))) # Write your code here.

print("y =", y)
