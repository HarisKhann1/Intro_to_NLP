from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize

words = word_tokenize('this is pretty cool tool !');
words_length = [len(w) for w in words]
print(words_length)

plt.hist(words_length);

plt.show()