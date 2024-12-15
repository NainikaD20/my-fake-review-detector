# Fake Review Detector

This project is a machine learning-based application designed to detect fake and computer generated reviews in text data. By leveraging natural language processing (NLP) techniques, the system analyzes text reviews and predicts whether they are fake or real. The application uses a logistic regression model, trained on a dataset of reviews, along with text preprocessing techniques like TF-IDF (Term Frequency-Inverse Document Frequency) to process the text data.

The app exposes a Flask-based API that accepts review text and returns predictions about its authenticity.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
  - [API Usage](#api-usage)
  - [Front-End Usage](#front-end-usage)
- [Model Training](#model-training)
- [API Endpoints](#api-endpoints)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## Overview
The Fake Review Detector application is a web-based service that predicts whether a review is "fake" or "real". The system involves the following components:
- **Data Preprocessing**: Converts the review text to lowercase and applies TF-IDF to transform it into numerical features.
- **Model Training**: A logistic regression model is trained on the preprocessed data to classify reviews.
- **Flask API**: A Flask-based API allows users to submit review text and get predictions on whether the review is fake or real.
- **Front-End**: A user-friendly interface built with HTML/CSS for easy interaction with the app.

## Technologies Used
- Python
- Flask (for the web API)
- scikit-learn (for machine learning models)
- pandas (for data manipulation)
- NumPy (for numerical operations)
- SciPy (for sparse matrix handling)
- Pickle (for saving and loading the model and transformers)
- Flask-CORS (for enabling CORS in the API)
- HTML/CSS (for the front-end)
- Jupyter Notebooks (for exploratory data analysis)

## Installation Instructions
To run the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/NainikaD20/my-fake-review-detector.git
    cd my-fake-review-detector
    ```

2. **Set up a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:

    ```bash
    python app.py
    ```

    The API will run on your localhost.

## Usage

### API Usage
The following API endpoint allows you to send reviews and get predictions:

- **POST /predict**: Accepts a POST request with a JSON payload containing the review text and returns the prediction (fake or real) along with probabilities.

### Front-End Usage
If you're using the front-end, follow these steps:

1. Open the app in your browser.
2. Enter a review in the text box and click "Submit."
3. View the results below, including the prediction and probabilities.

### Model Training
The model training process involves the following steps:

1. **Loading the dataset**: The dataset is loaded and cleaned (missing values removed, text converted to lowercase).
2. **Text Vectorization**: Use `CountVectorizer` and `TfidfTransformer` to convert review text into numerical features.
3. **Model Training**: Train a `LogisticRegression` model using the preprocessed data.
4. **Saving the model**: The trained model and transformers are saved using pickle.

To train the model, run:
python train_model.py

This will output a trained model file (`model.pkl`) and transformers (`bow_transformer.pkl`, `tfidf_transformer.pkl`), which can be used for later predictions.

### API Endpoints

#### `/predict`
- **Method**: POST
- **Request**: A JSON object containing the review text (key: "text").
- **Response**: A JSON object containing the prediction and probabilities.
- 
### Screenshots
![Screenshot 1](./images/Screenshot%20(82).png)
![Screenshot 2](./images/Screenshot%20(83).png)
### Features
- **Prediction**: Classifies reviews as fake or real.
- **Probability Scores**: Provides the probability that a review is fake or real.
- **CORS Enabled**: Supports cross-origin requests, enabling easy interaction with web applications.
- **Easy to Deploy**: The app can be easily deployed to any server or cloud service for production use.

### Contributing
To contribute to the project:

1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

