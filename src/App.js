import React, { useState } from "react";
import "./App.css";

function App() {
  const [review, setReview] = useState("");
  const [analysisResult, setAnalysisResult] = useState("");

  const handleInputChange = (event) => {
    setReview(event.target.value);
  };

  const analyzeReview = () => {
    if (review.trim() === "") {
      setAnalysisResult("Please enter a review to analyze.");
    } else {
      // Simulating the result for now
      setAnalysisResult("This review seems genuine!");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Fake Review Detector</h1>
        <textarea
          placeholder="Enter a review here..."
          value={review}
          onChange={handleInputChange}
          rows="5"
          cols="40"
        />
        <br />
        <button onClick={analyzeReview}>Analyze Review</button>
        <p>{analysisResult}</p>
      </header>
    </div>
  );
}

export default App;
