import nltk
import re
import numpy as np
import heapq


text = "NLTK is a powerful tool for natural language processing. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for tokenization, parsing, classification, stemming, tagging, and semantic reasoning."

dataset=nltk.sent_tokenize(text)
for i in range(len(dataset)):
    dataset[i]=dataset[i].lower()
    dataset[i]=re.sub(r'\W',' ',dataset[i])
    dataset[i]=re.sub(r'\s+',' ',dataset[i])

word2count={}
for data in dataset:
    words=nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word]=1
        else:
            word2count[word]+=1


freq_words = heapq.nlargest(400, word2count, key=word2count.get)

X = [] 
for data in dataset: 
    vector = [] 
    for word in freq_words: 
        if word in nltk.word_tokenize(data): 
            vector.append(1) 
        else: 
            vector.append(0) 
    X.append(vector) 
X = np.asarray(X) 

print(X)
print(freq_words)