import React, { useState } from 'react';

function App() {
  const [review, setReview] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ review }),
    });

    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div>
      <h1>Fake Review Detector</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={review}
          onChange={(e) => setReview(e.target.value)}
          placeholder="Enter your review"
        />
        <button type="submit">Predict</button>
      </form>
      <p>Prediction: {prediction}</p>
    </div>
  );
}

export default App;