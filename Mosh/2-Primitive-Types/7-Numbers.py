#......In python we have three types of numbers: integers, floating-point numbers and complex numbers. 

# --- Integers ---
# Integers are whole numbers without a decimal point. They can be positive, negative, or zero.
age = 30
print(age)  # Output: 30  
# --- Floating-point numbers ---
# Floating-point numbers are numbers with a decimal point. They can also be in scientific notation.
price = 19.99
print(price)  # Output: 19.99
# --- Complex numbers ---
# Complex numbers consist of a real part and an imaginary part, denoted by 'j' in Python.
complex_number = 2 + 3j
print(complex_number)  # Output: (2+3j) 
# --- Type conversion ---
# You can convert between different numeric types using built-in functions.
# Convert an integer to a float
float_age = float(age)
print(float_age)  # Output: 30.0
# Convert a float to an integer (note: this will truncate the decimal part)
int_price = int(price)
print(int_price)  # Output: 19
# Convert an integer to a complex number
complex_age = complex(age)
print(complex_age)  # Output: (30+0j)   
# --- Arithmetic operations ---
# You can perform various arithmetic operations on numbers.
a = 10
b = 3
print(a + b)  # Output: 13 (addition)
print(a - b)  # Output: 7 (subtraction)
print(a * b)  # Output: 30 (multiplication)
print(a / b)  # Output: 3.3333333333333335 (division)
print(a // b) # Output: 3 (floor division)
print(a % b)  # Output: 1 (modulus)
print(a ** b) # Output: 1000 (exponentiation)   

