import logging
from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS  # type: ignore # Import CORS
import pickle

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load the trained model and transformers
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('bow_transformer.pkl', 'rb') as f:
    bow_transformer = pickle.load(f)

with open('tfidf_transformer.pkl', 'rb') as f:
    tfidf_transformer = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    logging.info(request.get_json())  # Log the raw JSON input
    # Get the text from the request
    input_text = request.json.get('text')
    
    if not input_text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Preprocess the input text: convert to lowercase
    input_text = input_text.lower()

    # Transform the input text using the same BOW and TF-IDF transformations
    bow = bow_transformer.transform([input_text])
    tfidf_input = tfidf_transformer.transform(bow)

    # Make the prediction
    prediction = model.predict(tfidf_input)
    
    return jsonify({'prediction': str(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
