# We will make use of printing the output to console so let's introduce print function.
# Functions will be introduced later on but for now we only need the ability to print the value of an expression.
# Default behavior of the print function is as follows:
# 0. Calling print without any argument will print a new line.
print()
# 1. Printing one value will simply output it to the console.
print(1)  # Printing an integer.
print(1.2)  # Printing a floating-point number.
print(1+2j)  # This one is surrounded in parentheses when printed. I'll drop complex type for simplicity.
print([1, 2, 3])  # Printing a list.
print('Some text')  # Printing a str
print((1, 2, 3))  # Printing a tuple
# 2. Printing multiple values separated by a single space.
print(12, 34, 56)
print([1, 2, 3], [4, 5])
print('1', '2', '3')
print(1, 2, 3, 'test', [2])

# Prettifying the output by adding new lines
print()
print()


# Let's check operations on basic types:
print('Basic arithmetic operations')
print('1 + 2 =', 1 + 2)  # Addition: int + int
print('3 - 7 =', 3 - 7)  # Subtraction: int - int
print('2 * 4 =', 2 * 4)  # Multiplication: int * int
print('8 / 4 =', 8 / 4)  # Division: int / int
print('8 % 4 =', 8 % 4)  # Remainder of division: int / int
print()
print('Simple explanation of modulo division (%):')
print('7 / 4 =', 7 / 4)
print('7 % 4 =', 7 % 4)
print('7 / 4 + 7 % 4 = 7')
print('4 * 1 + 3 = 7')
print('4 (divisor) * 1 (quotient) + 3 (remainder) = 7 (dividend)')
print()
print('Now carefully observe this:')
print('2 / 4 =', 2 / 4, 'This works in Python 3+ as you would expect: 0.5')  # Division: int / int
print('2 // 4 =', 2 // 4)  # Integer division: int // int
print('Dividing int by int returns the result as int without the fractional part!')
print('You need to convert one of the ints to float to get the expected result:')
print('2.0 / 4 =', 2.0 / 4)  # Division: float / int
print('2.0 // 4 =', 2.0 // 4)  # Integer division: float // int
print('2 / 4.0 =', 2 / 4.0)  # Division: int / float
print('2 // 4.0 =', 2 // 4.0)  # Integer division: int // float
print('float(2) / 4 =', float(2) / 4)  # Division: float / int
print('float(2) // 4 =', float(2) // 4)  # Integer division: float // int
