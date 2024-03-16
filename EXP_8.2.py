import nltk
import re
import numpy as np

# Sample text
text = "NLTK is a powerful tool for natural language processing. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for tokenization, parsing, classification, stemming, tagging, and semantic reasoning."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Clean the words (remove non-alphanumeric characters and convert to lowercase)
words = [word.lower() for word in words if re.match('^[a-zA-Z]+$', word)]

# Create a dictionary to store word counts
word_counts = {}

# Count occurrences of each word
for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Get the unique words (vocabulary)
vocabulary = sorted(word_counts.keys())

# Create a matrix to represent Bag-of-Words
bow_matrix = np.zeros((len(words), len(vocabulary)))

# Populate the matrix with word counts
for i, word in enumerate(words):
    for j, vocab_word in enumerate(vocabulary):
        if word == vocab_word:
            bow_matrix[i, j] += 1

print("Bag-of-Words Matrix:")
print(bow_matrix)
print("\nVocabulary:")
print(vocabulary)
