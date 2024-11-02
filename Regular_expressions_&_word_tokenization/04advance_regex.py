from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
print('\nFirst task:');
print(regexp_tokenize(my_string, r"(\w+|\?|!)"))
print(regexp_tokenize(my_string, r"(\w+|#\d|\?|!)"))


# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"

# Sample tweets list
tweets = [
    "Just setting up my #twitter #firsttweet!",
    "Learning Python is fun! #coding #python",
    "NLP is amazing! @bootcamp #NLP #MachineLearning"
]

# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)
print(f'\nSecond task:');
print(hashtags)

# Write a pattern that matches both mentions and hashtags
pattern2 = r"([#|@]\w+)"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print('\nThird task:');
print(mentions_hashtags)

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer() 
all_tokens = [tknzr.tokenize(t) for t in tweets]
print('\nFourth task:');
print(all_tokens)

