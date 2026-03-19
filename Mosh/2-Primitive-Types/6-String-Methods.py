course = "Python for Beginners"

# --- String Methods ---
# Python provides many built-in methods to manipulate strings. Here are some common ones:
# --- upper() and lower() ---
# Convert a string to uppercase or lowercase
print(course.upper())   # Output: PYTHON FOR BEGINNERS
print(course.lower())   # Output: python for beginners  
# --- title() ---
# Convert the first character of each word to uppercase
print(course.title())   # Output: Python For Beginners
# --- strip() ---
# Remove leading and trailing whitespace
whitespace_str = "   Hello, World!   "
print(whitespace_str.strip())  # Output: Hello, World!
# --- replace() ---
# Replace occurrences of a substring with another string
print(course.replace("Beginners", "Everyone"))  # Output: Python for Everyone
# --- find() ---
# Find the index of the first occurrence of a substring
print(course.find("for"))  # Output: 7 (index of 'f' in 'for')
# --- split() ---
# Split a string into a list of substrings based on a delimiter (default is space)
print(course.split())  # Output: ['Python', 'for', 'Beginners']
# --- join() ---
# Join a list of strings into a single string with a specified separator
words = ["Python", "is", "awesome"]
print(" ".join(words))  # Output: Python is awesome 

# --- in operator ---
# Check if a substring exists in a string
print("Python" in course)  # Output: True
print("Java" in course)    # Output: False