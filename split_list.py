# Given list and the length of the first part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3

# Split the list into two parts
first_part = original_list[:length_of_first_part]
second_part = original_list[length_of_first_part:]

# Output the two parts
print("Splitted the said list into two parts:", (first_part, second_part))
