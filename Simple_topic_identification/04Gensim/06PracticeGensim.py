# Import Dictionary
from gensim.corpora.dictionary import Dictionary

# List of articles
articles = [
    ["human", "interface", "computer"],
    ["survey", "user", "computer", "system", "response", "time"],
    ["eps", "user", "interface", "system"],
    ["system", "human", "system", "eps"],
    ["user", "response", "time"],
    ["trees"],
    ["graph", "trees"],
    ["graph", "minors", "trees"],
    ["graph", "minors", "survey"]
]


# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])

print(dictionary.get(6))
