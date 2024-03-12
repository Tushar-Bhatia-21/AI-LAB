import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Sample text
text = "NLTK is a powerful tool for natural language processing. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for tokenization, parsing, classification, stemming, tagging, and semantic reasoning."

# Tokenization
tokens = word_tokenize(text)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]

# Stop words removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print("Original Text:")
print(text)
print("\nTokenization:")
print(tokens)
print("\nLemmatization:")
print(lemmatized_tokens)
print("\nStemming:")
print(stemmed_tokens)
print("\nStop Words Removal:")
print(filtered_tokens)
