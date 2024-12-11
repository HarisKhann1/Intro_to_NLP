import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Example article text
article = "Your article text goes here."
article = """
The quick brown fox jumps over the lazy dog. This sentence contains every letter in the English alphabet. 
Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. 
The ultimate objective of NLP is to read, decipher, understand, and make sense of the human languages in a manner that is valuable. 
Most NLP techniques rely on machine learning to derive meaning from human languages. 
NLP is used to apply algorithms to identify and extract the natural language rules such that the unstructured language data is converted into a form that computers can understand. 
When the text has been provided, the computer will utilize algorithms to extract meaning associated with every sentence and collect the essential data from them.
"""


# Tokenize the article into sentences: sentences
sentences = sent_tokenize(article)

# Tokenize each sentence into words: token_sentences
token_sentences = [word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 

# Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)
# for sent in chunked_sentences:
#     print(sent)
# print()    

# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print('NE Tags',chunk)
