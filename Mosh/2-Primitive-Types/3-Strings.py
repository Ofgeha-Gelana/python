# ===========================
# STRINGS IN PYTHON
# ===========================

course_name = "Python Programming"  # Fixed typo: "Pyhton" -> "Python"

# --- Length ---
# len() returns the number of characters in the string
print(len(course_name))        # Output: 18

# --- Indexing ---
# Positive index: starts from 0 (left)
print(course_name[0])          # Output: P  (first character)
# Negative index: starts from -1 (right)
print(course_name[-1])         # Output: g  (last character)

# --- Slicing: string[start:end] ---
# 'end' is exclusive (not included in the result)
print(course_name[0:3])        # Output: Pyt  (index 0, 1, 2)
print(course_name[0:])         # Output: Python Programming  (from index 0 to end)
print(course_name[:3])         # Output: Pyt  (from start to index 2)
print(course_name[:])          # Output: Python Programming  (full copy of string)