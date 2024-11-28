# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert the sentence to lowercase
sentence = sentence.lower()

#replace punctuation marks (optional, but helps in clean counting)
sentence = sentence.replace('.', '').replace(',', '')

#split the sentence into words
words = sentence.split()

#initialize an empty list to store the words and their counts
word_list = []

# Loop through each word in the list of words
for word in words:
    found = False
    for item in word_list:
        if item[0] == word:
            item[1] += 1  
            found = True
            break
    
    # If the word is not found in the word_list, add it with a count of 1
    if not found:
        word_list.append([word, 1])

# Print the word counts
for item in word_list:
    print(f"'{item[0]}': {item[1]}")



    
