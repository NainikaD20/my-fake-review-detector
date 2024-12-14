import React, { useState } from 'react';
import './App.css'; // Import the CSS file

function App() {
  const [review, setReview] = useState('');
  const [prediction, setPrediction] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setPrediction('');

    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',  // Ensure this is POST
      headers: { 
        'Content-Type': 'application/json' 
      },
      body: JSON.stringify({ text: review }) // Update key to 'text'
,  // Send the data as JSON
    });
    

    const data = await response.json();
    setPrediction(data.prediction);
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>Fake Review Detector</h1>
      <div className="card">
        <form onSubmit={handleSubmit}>
          <textarea
            value={review}
            onChange={(e) => setReview(e.target.value)}
            placeholder="Enter your review"
            style={{ boxSizing: 'border-box', width: '100%' }}
          />
          <button type="submit">Predict</button>
        </form>
        {loading && <div className="loader"></div>}
        {prediction && (
          <p className={`prediction ${prediction.toLowerCase()}`}>
            {prediction === 'Real' ? '✅ This review seems Real!' : '❌ This review seems Fake!'}
          </p>
        )}
      </div>
    </div>
  );
}

export default App;
