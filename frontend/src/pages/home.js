import "./home-files/home.css";
import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Pdf from "./home-files/pdf-upload";

export default function Home() {
    return (
        // container for the whole of the home page 
        <div className="home-page-container">
            {/** heading display */}
            <div className="home-container">
                <h1>Home</h1>
            </div>
            {/**pdf container */}
            <div className="pdf-container">
                <Pdf />
            </div>
        </div>
    );
}