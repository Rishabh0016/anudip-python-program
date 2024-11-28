#Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 3, 2, 8, 9, 1]

# Initialize an empty list to store duplicates
duplicates = []

# Initialize an empty list to track seen numbers
seen = []

# Loop through the list and find duplicates
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.append(num) 

# Output the list of duplicates
print("Duplicate values:", duplicates)

