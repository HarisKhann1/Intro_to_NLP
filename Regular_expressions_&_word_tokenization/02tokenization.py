from nltk.tokenize import word_tokenize, sent_tokenize
scene_one = "Hello there! How are you doing today? This is a test sentence. I hope you are enjoying learning NLP. Tokenization is the first step in text processing. Let's see how it works."

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)
# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenize_sent = word_tokenize(sentences[3])
print(tokenize_sent)
# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

print(unique_tokens)