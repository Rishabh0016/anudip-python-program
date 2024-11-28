# Given string
string = "Welcome to python Training"

# Initialize a counter for vowels
vowel_count = 0

# List of vowels
vowels = "aeiouAEIOU"

# List to store the vowels found in the string
vowel_letters = []

# Loop through each character in the string
for char in string:
    if char in vowels:  # Check if the character is a vowel
        vowel_count += 1
        vowel_letters.append(char)

# Output the count of vowels
print("Number of vowels:", vowel_count)

# Output the vowels found in the string
print("Vowels found in the string:", ", ".join(vowel_letters))


