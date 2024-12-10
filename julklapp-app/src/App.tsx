import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Julklap from './components/Julklap/Julklap';
import './App.css'; // Import the styles.css file
import Navbar from './components/Navbar/Navbar';
import About from './components/About/About';
import Contact from './components/Contact/Contact';


function App() {
  return (
    <Router>
      <div className="navbar-wrapper">
        <Navbar />
      </div>
      <div className="container">
        <Routes>
          <Route path="/" element={<Julklap />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;