"""
Why preprocess?
• Helps make for better input data
• When performing machine learning or other statistical
methods
• Examples:
• Tokenization to create a bag of words
• Lowercasing words
• Lemmatization/Stemming
• Shorten words to their root stems
• Removing stop words, punctuation, or unwanted tokens
• Good to experiment with different approaches
"""

"""
Preprocessing example
• Input text: Cats, dogs and birds are common pets. So are fish.
• Output tokens: cat, dog, bird, common, pet, fish 
Note:
    text is converted to lower case and removed stop words and convert it to base form
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer

# print(stopwords.words('english')); # stopwords in english language

text = "The cat is in 33 the box. The $ cat likes the box. The box is over the cat."

# create tokens from the above text only the aplhabets not numbers and special characters
tokens = [word for word in word_tokenize(text.lower()) if word.isalpha()]
print(tokens)

# remove all the stop words in tokens list
remove_stop_words = [stop for stop in tokens if stop not in stopwords.words('english')]
print(remove_stop_words)
print(Counter(remove_stop_words).most_common(2))

# Lemmatization
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in remove_stop_words]
print(tokens)
