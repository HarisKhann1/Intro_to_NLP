from nltk import word_tokenize
from gensim.corpora.dictionary import Dictionary

# List of documents to be processed
my_documents = ["The movie was about a spaceship and aliens.",
                "I really enjoyed the movie!",
                "Awesome action scenes, but boring characters.",
                "The movie was awful! I hate alien films.",
                "Space is cool! I liked the movie.",
                "More space films, please!"
                ]

# Convert each document to lowercase and tokenize it
# Tokenization is the process of splitting text into individual words or tokens
tokenized_docs = [word_tokenize(document.lower()) for document in my_documents]
print(f'Tokenized_documents:\n-------------------\n{tokenized_docs}')

# Create a dictionary representation of the documents
# The dictionary maps each word to a unique id
dictionary = Dictionary(tokenized_docs)
print("\nMapping of words in Gensim library\n")
print(dictionary.token2id)

# Create a bag-of-words representation of the documents
# Each document is represented as a list of tuples (word_id, word_frequency)
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
print("\nBow of word showing key and frequency\n")
print(corpus)

'''
# retrieving the actual token based on the token id
token = [dictionary[id] for id, freq in corpus[0]]
print(token)
'''

# in corpors zeroth index which tuple in tuple we want the first token id
print(dictionary[corpus[0][1][0]]) 

# taking id of a particular token
print(dictionary.token2id.get("awesome"))

# taking actual token based on the id
print(dictionary.get(15))
