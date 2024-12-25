from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np

"""data = {
    "Text": [
        "Breaking news fake story",
        "This is a real and true story",
        "Another fake story spreads online",
        "Real news updates daily"
    ],
    "Label": ["FAKE", "REAL", "FAKE", "REAL"]
}
"""
# Sample documents
documents = [
    "I love machine learning",
    "I love programming",
    "Machine learning is great"
]

# Create TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

# Fit and transform the documents into a sparse matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Get the dense matrix (full representation)
dense_matrix = tfidf_matrix.toarray()

# Display the feature names (vocabulary)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Display dense matrix
print("Dense Matrix:")
print(dense_matrix)

# Display the feature names (vocabulary)
print("\nFeature Names (Vocabulary):")
print(feature_names)

# The sparse matrix (non-zero elements) can also be displayed as:
print("\nSparse Matrix:")
print(tfidf_matrix)



