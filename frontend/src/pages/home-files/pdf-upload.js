import axios from "axios";
import React, { Component } from "react";

class Pdf extends Component {
  state = {
    selectedFile: null,
    textInput: '', // Added state for the text input
    isFormValid: false, // Added state to track if the form is valid for submission
  };

  onFileChange = (event) => {
    this.setState({
      selectedFile: event.target.files[0],
    }, this.validateForm);
  };

  onTextInputChange = (event) => {
    this.setState({
      textInput: event.target.value,
    }, this.validateForm);
  };

  // Function to validate the form
  validateForm = () => {
    const { selectedFile, textInput } = this.state;
    this.setState({
      isFormValid: selectedFile !== null && textInput.trim() !== ''
    });
  };

  onFileUpload = () => {
    const formData = new FormData();
    formData.append(
      "myFile",
      this.state.selectedFile,
      this.state.selectedFile.name
    );

    // Append text input to the formData if you want to send them together
    formData.append("textInput", this.state.textInput);

    // single API endpoint that handles both file and text input
    axios.post("http://localhost:5000/api/upload", formData)
      .then(response => {
        console.log("File and text input uploaded successfully");
        alert("file and text input uploaded");
      })
      .catch(error => {
        console.error("Error uploading file and text input:", error);
        //alert("nope, did not work");
        alert(error);
      });
  };

// File content to be displayed after
	// file upload is complete
    fileData = () => {
		if (this.state.selectedFile) {
			return (
				<div>
					<h2>File Details:</h2>
					<p>
						File Name:{" "}
						{this.state.selectedFile.name}
					</p>

					<p>
						File Type:{" "}
						{this.state.selectedFile.type}
					</p>

					<p>
						Last Modified:{" "}
						{this.state.selectedFile.lastModifiedDate.toDateString()}
					</p>
				</div>
			);
		} else {
			return (
				<div>
					<br />
					<h5>
						Please choose a file and enter a job description before Pressing the Upload
						button 
					</h5>
				</div>
			);
		}
	};  

  render() {
    return (
      <div>
        <h3>Please upload your resume as a PDF and copy/paste your target job description!</h3>
        <div>
            {/**only accept pdfs */}
            <input type="file" onChange={this.onFileChange} accept="application/pdf"/>
            <button onClick={this.onFileUpload} disabled={!this.state.isFormValid}>
                Upload!
            </button>
        </div>
        <div className="job-description-container">
          {this.fileData()}
          <textarea
            placeholder="Enter the job description here..."
            onChange={this.onTextInputChange}
            rows="5" // adjust as needed to increase height
            cols="40" // adjust as needed to increase width
          ></textarea>
        </div>
      </div>
    );
  }
}

export default Pdf;
