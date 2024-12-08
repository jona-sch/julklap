import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Homepage from './components/Homepage';
import './App.css'; // Import the styles.css file
function App() {
  return (
  <Router>
  <div className="container">
  <Routes>
  <Route path="/" element={<Homepage />} />
  </Routes>
  </div>
  </Router>
  );
  }
export default App;