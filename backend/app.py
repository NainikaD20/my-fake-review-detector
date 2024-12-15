import pickle
import scipy.sparse
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Load the saved model and transformers
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('bow_transformer.pkl', 'rb') as f:
    bow_transformer = pickle.load(f)

with open('tfidf_transformer.pkl', 'rb') as f:
    tfidf_transformer = pickle.load(f)

# Prediction function
def predict_review(review):
    # Step 1: Clean and transform the input text
    # Convert the review text to lowercase
    review = review.lower()
    
    # Convert to bag-of-words features
    bow_features = bow_transformer.transform([review])
    
    # Convert to TF-IDF features
    tfidf_features = tfidf_transformer.transform(bow_features)
    
    # Step 2: Get prediction probabilities (fake vs true)
    prob_fake, prob_real = model.predict_proba(tfidf_features)[0]
    
    # Step 3: Determine the prediction label based on the probabilities
    prediction = 'CG' if prob_fake > prob_real else 'OR'
    
    return prediction, prob_fake, prob_real

# Endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('text')  # Get the review text from the request
    
    # Make prediction
    prediction, prob_fake, prob_real = predict_review(review)
    print(prediction, prob_fake, prob_real)
    # Return the result as a JSON response
    return jsonify({
        'prediction': prediction,
        'fake_probability': prob_fake,
        'real_probability': prob_real
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
