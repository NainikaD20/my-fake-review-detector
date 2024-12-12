from flask import Flask, jsonify, request
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load your pre-trained model (replace with the actual model)
# Example: model = pickle.load(open('model.pkl', 'rb'))
# For now, we can just mock the prediction step.
def predict_fake_review(review):
    # Mock function that predicts a fake review (this should be replaced with your model logic)
    return "fake" if "bad" in review.lower() else "real"

@app.route('/predict', methods=['POST'])
def predict():
    # Get review text from request body
    data = request.get_json()
    review_text = data.get('review')

    # Call prediction function
    prediction = predict_fake_review(review_text)

    # Return prediction as JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
