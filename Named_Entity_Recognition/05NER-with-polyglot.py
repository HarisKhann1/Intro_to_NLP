from sklearn.model_selection import train_test_split

# Example dataset
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Split data into train and test sets with random_state=42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print("Train data:", X_train)
print("Test data:", X_test)
print("Train data:", y_train)
print("Test data:", y_test)
