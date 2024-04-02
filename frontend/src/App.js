import React from "react";
import "./styles.scss";
import CustomNav from "./navbar-components/navbar.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home.js";
import Results from "./pages/results.js";

export default function App() {
  return (
    <div className="app-container">
      <Router>
        <CustomNav
          li={[
            ["Home", "img/home.png", "/home"],
            ["Results", "img/home.png", "/results"],
            // Update other items as necessary, ensuring you provide the correct paths
          ]}
        />
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/results" element={<Results />} />
          {/* Define other routes here */}
        </Routes>
      </Router>
    </div>
  );
}
