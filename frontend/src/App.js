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
            // update roots as needed
          ]}
        />
        <Routes>
          {/*initial path set to home. /home also set in case someone navigates away, then back to home */}
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </Router>
    </div>
  );
}
