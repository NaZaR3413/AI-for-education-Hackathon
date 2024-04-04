import "./results-files/results.css";
import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Chart from "./results-files/chart";

export default function Results() {
    return (
        <div className="results-page-container">
            <div className="top-half">
                <div className="chart-heading">
                    <h1>Results</h1>
                </div>
                <div className="chart-display">
                    <Chart />
                </div>
            </div>

            <div className="bottom-half">

            </div>
        </div>
    );
  }