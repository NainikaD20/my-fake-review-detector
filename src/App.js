import React, { useState } from "react";

function App() {
  const [review, setReview] = useState("");
  const [prediction, setPrediction] = useState("");

  const handleInputChange = (e) => {
    setReview(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Send review to the Flask API
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ review })
    });

    const data = await response.json();
    setPrediction(data.prediction); // Update prediction state with result
  };

  return (
    <div className="App">
      <h1>Fake Review Detector</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={review}
          onChange={handleInputChange}
          placeholder="Enter your review here"
          rows="5"
        />
        <button type="submit">Submit</button>
      </form>
      <p>Prediction: {prediction}</p>
    </div>
  );
}

export default App;
