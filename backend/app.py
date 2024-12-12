from flask import Flask, jsonify, request
from textblob import TextBlob

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

def predict_fake_review(review):
    blob = TextBlob(review)
    # A simple sentiment analysis approach, you can customize this
    if blob.sentiment.polarity < -0.5:
        return "fake"
    else:
        return "real"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review_text = data.get('review')

    prediction = predict_fake_review(review_text)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)