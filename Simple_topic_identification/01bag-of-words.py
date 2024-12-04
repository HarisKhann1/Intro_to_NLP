# Bag-of-words
    # • Basic method for finding topics in a text
    # • Need to first create tokens using tokenization
    # • ... and then count up all the tokens
    # • The more frequent a word, the more important it might be
    # • Can be a great way to determine the significant words in a text

# Bag-of-words example
    # • Text: "The cat is in the box. The cat likes the box. The box is over the cat."
    # • Bag of words (stripped punctuation):
    # • "The": 3, "box": 3
    # • "cat": 3, "the": 3
    # • "is": 2
    # • "in": 1, "likes": 1, "over": 1

from nltk.tokenize import word_tokenize
from collections import Counter #for to cound the alphabets in words

text = "The cat is in the box. The cat likes the box. The box is over the cat."

tokens = word_tokenize(text);
length_of_each_tokens = Counter(tokens)
print(length_of_each_tokens)

common_tokens = Counter.most_common(length_of_each_tokens,2) # returns the first 2 most common tokens and the rest of the tokens with same numbers of aplhabets will get ignore
print(common_tokens)

# or to covert the text into lower case to avoid case sentivity

lower_case_test = text.lower()
tokens = word_tokenize(lower_case_test);
print(Counter(tokens))
