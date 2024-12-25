# Import the necessary modules
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np

df = pd.read_csv('fake_or_real_news.csv')

# Print the head of df
print(df.head())

# Create a series to store the labels: y
y = df["label"]

print(df["text"].head())

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df["text"],y, test_size = 0.33, random_state = 53)

# Initialize a TfidfVectorizer object: tfidf_vectorizer
# TfidfVectorizer: Convert a collection of raw documents to a matrix of TF-IDF features.
# stop_words will be ignored and max_df show if a word appears in more than 70% of the documents, it will be ignored.
tfidf_vectorizer = TfidfVectorizer(stop_words = "english", max_df = 0.7)

# Transform the training data: tfidf_train 
tfidf_train = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data: tfidf_test 
tfidf_test = tfidf_vectorizer.transform(X_test)

# Print the first 10 features, first 10 vocabularies of the tfidf_vectorizer
print(tfidf_vectorizer.get_feature_names_out()[:10])

# Print the first 5 vectors of the tfidf training data
print(tfidf_train.A[:5])


nb_classifier = MultinomialNB()
nb_classifier.fit(tfidf_train, y_train)
pred = nb_classifier.predict(tfidf_test)
print(pred)
result = metrics.accuracy_score(y_test, pred)
print(f'\nPrediction:\n {result}')

# Calculate the confusion matrix: cm
cm = metrics.confusion_matrix(y_test, pred, labels = ['FAKE', 'REAL'])
print(cm)

# Create the list of alphas: alphas
alphas = np.arange(0, 1, 0.1)

# Define train_and_predict()
def train_and_predict(alpha):
    # Instantiate the classifier: nb_classifier
    nb_classifier = MultinomialNB(alpha = alpha)
    # Fit to the training data
    nb_classifier.fit(tfidf_train, y_train)
    # Predict the labels: pred
    pred = nb_classifier.predict(tfidf_test)
    # Compute accuracy: accuracy
    accuracy = metrics.accuracy_score(y_test, pred)
    return accuracy

# Iterate over the alphas and print the corresponding accuracy
for alpha in alphas:
    print(f'Alpha: {alpha}, Accuracy: {train_and_predict(alpha)}')