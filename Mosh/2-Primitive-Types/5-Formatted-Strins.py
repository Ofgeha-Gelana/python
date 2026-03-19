# ===========================
# FORMATTED STRINGS (f-strings)
# ===========================
# f-strings (introduced in Python 3.6) let you embed variables or
# expressions directly inside a string using curly braces {}.
# Syntax: f"text {variable} text"

first = "Ofgeha"
last = "Gelana"

# --- Old way: string concatenation ---
# Manually joining strings with + can get messy with many variables
full = first + " " + last
print(full)             # Output: Ofgeha Gelana

# --- Better way: f-string ---
# Cleaner and easier to read
full = f"{first} {last}"
print(full)             # Output: Ofgeha Gelana

# --- Expressions inside f-strings ---
# You can put any valid Python expression inside {}
print(f"{first} {last} has {len(first)} letters in their first name")
# Output: Ofgeha Gelana has 6 letters in their first name

# --- f-strings with numbers ---
price = 49.99
quantity = 3
print(f"Total: ${price * quantity:.2f}")   # Output: Total: $149.97
# :.2f formats the number to 2 decimal places
