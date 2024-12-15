import pickle
import pandas as pd
import scipy.sparse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load the preprocessed data (TF-IDF matrix) and labels
X_tfidf = scipy.sparse.load_npz('Preprocessed_new_Dataset.npz')  # Replace with your actual file name
y = pd.read_csv('labels.csv')  # Replace with the actual path to your labels

# Ensure that y is a 1D array
y = y.values.ravel()  # Flatten to 1D array if y is in 2D (for model training)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete and saved.") 