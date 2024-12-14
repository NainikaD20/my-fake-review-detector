import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import scipy.sparse  # For saving the sparse matrix
import pickle  # Add this import

# Step 1: Load the dataset
df = pd.read_csv('dataset/fake_reviews_dataset.csv')  # Adjust the path if necessary

# Step 2: Clean the data
df.dropna(inplace=True)  # Remove any rows with missing values
df['text_'] = df['text_'].str.lower()  # Convert all text to lowercase

# Step 3: Convert text to numerical features using TF-IDF
bow_transformer = CountVectorizer(stop_words='english')  # Create a bag-of-words model
tfidf_transformer = TfidfTransformer()  # TF-IDF transformer

# Convert the text data into a sparse matrix (count of words)
X_bow = bow_transformer.fit_transform(df['text_'])
X_tfidf = tfidf_transformer.fit_transform(X_bow)  # Transform the bag-of-words into TF-IDF

# Step 4: Save the TF-IDF matrix as a sparse matrix file (.npz)
scipy.sparse.save_npz('Preprocessed_new_Dataset.npz', X_tfidf)

# Optionally, save the labels (target column) to a CSV file
df['label'].to_csv('labels.csv', index=False)

# Save the transformers for later use
with open('bow_transformer.pkl', 'wb') as f:
    pickle.dump(bow_transformer, f)

with open('tfidf_transformer.pkl', 'wb') as f:
    pickle.dump(tfidf_transformer, f)

print("Preprocessing complete and data saved.")
