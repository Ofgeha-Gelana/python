# ===========================
# ESCAPE SEQUENCES IN PYTHON
# ===========================
# Escape sequences let you include special characters inside strings.
# They start with a backslash (\).
#
# Common escape sequences:
#   \"   -> double quote
#   \'   -> single quote
#   \\   -> literal backslash
#   \n   -> newline (moves to next line)
#   \t   -> tab (horizontal indent)

course = "Python Programming"

# --- \" : Embedding double quotes inside a double-quoted string ---
course = "Python \"Programming\""
print(course)           # Output: Python "Programming"

# --- Alternative: mix quote types to avoid escaping ---
course = 'Python "Programming"'
print(course)           # Output: Python "Programming"

# --- \' : Embedding single quotes inside a single-quoted string ---
msg = 'It\'s a great course'
print(msg)              # Output: It's a great course

# --- \\ : Literal backslash (e.g. for file paths) ---
path = "C:\\Users\\ofge\\Documents"
print(path)             # Output: C:\Users\ofge\Documents

# --- \n : Newline ---
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# --- \t : Tab ---
print("Name:\tPython")  # Output: Name:   Python
