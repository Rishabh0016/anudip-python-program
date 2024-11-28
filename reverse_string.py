# Given string
string = "Deeptech Python Training"

# Split the string into words
words = string.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed words back into a single string
reversed_string = " ".join(reversed_words)

# Output the reversed string
print("Reversed words string:", reversed_string)
