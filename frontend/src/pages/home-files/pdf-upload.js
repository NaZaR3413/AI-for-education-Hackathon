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

    // You can use a single API endpoint that handles both file and text input
    axios.post("api/upload", formData)
      .then(response => {
        console.log("File and text input uploaded successfully");
      })
      .catch(error => {
        console.error("Error uploading file and text input:", error);
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
					<h4>
						Choose a file and enter a job description before Pressing the Upload
						button Please
					</h4>
				</div>
			);
		}
	};  

  render() {
    return (
      <div>
        <h3>Please upload your resume as a PDF and copy/paste your target job description!</h3>
        <div>
            <input type="file" onChange={this.onFileChange} accept="application/pdf"/>
            <button onClick={this.onFileUpload} disabled={!this.state.isFormValid}>
                Upload!
            </button>
        </div>
        <div>
          <textarea
            placeholder="Enter the job description here..."
            onChange={this.onTextInputChange}
            rows="5" // You can set the number of rows to increase its height
            cols="33" // You can set the number of columns to increase its width
          ></textarea>
        </div>
        {this.fileData()}
      </div>
    );
  }
}

export default Pdf;
