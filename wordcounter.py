def count_words(text):
    # Split the text into words
    words = text.split()
    
    # Count the total number of words
    total_words = len(words)
    
    # Count the frequency of each word
    word_frequency = {}
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    return total_words, word_frequency

# Get input from the user
input_text = input("Enter your text: ")

# Count words
total_count, word_counts = count_words(input_text)

# Display results
print(f"\nTotal number of words: {total_count}")
print("\nWord frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
