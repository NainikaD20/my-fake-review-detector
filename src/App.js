import React, { useState } from 'react';
import './App.css';

function App() {
  const [review, setReview] = useState('');
  const [prediction, setPrediction] = useState('');
  const [fakeProb, setFakeProb] = useState(null);
  const [realProb, setRealProb] = useState(null); 
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setPrediction('');
    setFakeProb(null);
    setRealProb(null); 

    // Simulating progress during prediction
    const interval = setInterval(() => {
      setProgress((oldProgress) => {
        if (oldProgress === 100) {
          clearInterval(interval);
        }
        return Math.min(oldProgress + 10, 100);
      });
    }, 500);

    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: review }),
      });

      const data = await response.json();
      setPrediction(data.prediction);
      setFakeProb(data.fake_probability);
      setRealProb(data.real_probability);
    } catch (error) {
      console.error('Error during prediction:', error);
    } finally {
      setLoading(false);
      setProgress(100);
    }
  };

  const fakeProbPercentage = fakeProb !== null && !isNaN(fakeProb) ? Math.round(fakeProb * 100) : 'N/A';
  const realProbPercentage = realProb !== null && !isNaN(realProb) ? Math.round(realProb * 100) : 'N/A';

  return (
    <div className="app-container">
      <h1>Fake Review Detector</h1>
      <div className="card">
        <form onSubmit={handleSubmit} className="review-form">
          <div className="input-container">
            <textarea
              value={review}
              onChange={(e) => setReview(e.target.value)}
              placeholder="Enter your review here..."
              className="review-input"
              maxLength="500"
            />
            <div className="character-count">{review.length}/500 characters</div>
          </div>
          <button type="submit" className="submit-btn">Detect</button>
        </form>

        {loading && (
          <div className="loading-container">
            <div className="progress-ring" style={{ 
              background: `conic-gradient(#0066cc ${progress}%, #e0e0e0 ${progress}%)` 
            }}>
              <div className="progress-text">{progress}%</div>
            </div>
            <p>Analyzing...</p>
          </div>
        )}

        {prediction && (
          <div className="result-card">
            <h3 className={`prediction ${prediction}`}>
              {prediction === 'OR' ? '✅ This review is real!' : '❌ This review is fake!'}
            </h3>
            <div className="probability-container">
              <p><strong>Probability of being real:</strong> {realProbPercentage}%</p>
              <p><strong>Probability of being fake:</strong> {fakeProbPercentage}%</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
