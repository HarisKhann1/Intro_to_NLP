import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, regexp_tokenize

dataset1 = [
    "Hello, world! This is a test sentence.",
    "Regular expressions are powerful tools for text processing.",
    "Tokenization is the process of breaking down text into smaller units.",
    "Python is a great programming language for NLP tasks.",
    "Let's perform some text analysis using Python."
]

dataset2 = [
    "Hello, world! This is a test sentence with numbers like 123 and special characters #, $, &.",
    "Regular expressions are powerful tools for text processing. They can match patterns like dates (12/12/2020) or emails (example@example.com).",
    "Tokenization is the process of breaking down text into smaller units. For example, splitting 'don't' into 'do' and 'n't'.",
    "Python is a great programming language for NLP tasks. It supports libraries like NLTK, SpaCy, and more.",
    "Let's perform some text analysis using Python. We'll analyze sentences, words, and even punctuation marks!"
]

long_paragraph = "Natural Language Processing (NLP) is a fascinating field of study. It involves the interaction between computers and human language. NLP techniques are used to analyze and understand large amounts of natural language data. Applications of NLP include language translation, sentiment analysis, and speech recognition."


# applying sentence tokenization on long_paragraph
sentence_tokenization = sent_tokenize(long_paragraph)
print(f'Sentence tokenization on long paragraph:\n\n{sentence_tokenization}')

word_tokenization = [word_tokenize(sentence) for sentence in dataset1]
print()
print(f'sentence tokenization in dataset1:\n\n{word_tokenization}')

# flat the word_tokenization array

word_token_flate_array = [item for sublist in word_tokenization for item in sublist]
print()
print(f'Flated Array, all word tokens array:\n\n{word_token_flate_array}')





# Practice questions for NLTK regex on the datasets

# 1. Write a regex pattern to find all sentences that contain numbers in dataset2.
pattern = r"[\d]+"
number_in_dataset1 = [sentence for sentence in dataset2]
print()
print(number_in_dataset1)

sentences_contains_digits = [
    sentence
    for paragraph in dataset2
    for sentence in sent_tokenize(paragraph)
    if regexp_tokenize(sentence, pattern)
]
print('\n\nQuestion NO.1')
print(sentences_contains_digits)

# 2. Write a regex pattern to find all sentences that contain special characters in dataset2.
pattern2 = r"[\@#&!]"

special_character = [
    sentence
    for paragraph in dataset2
    for sentence in sent_tokenize(paragraph)
    if regexp_tokenize(sentence, pattern2)
]

print('\n\nQuestion NO.2')
print(special_character)

# 3. Write a regex pattern to find all sentences that contain email addresses in dataset2.
pattern3 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email_sentences = [
    sentence
    for paragraph in dataset2
    for sentence in sent_tokenize(paragraph)
    if regexp_tokenize(sentence, pattern3)
]

print('\n\nQuestion NO.3')
print(email_sentences)
