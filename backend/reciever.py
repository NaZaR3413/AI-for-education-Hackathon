from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow all domains

@app.route('/api/upload', methods=['POST'])
def upload_file_and_text():
    text_input = request.form['textInput']  # Get the text input from FormData
    file = request.files['myFile']  # Get the file from FormData
    
    print(text_input) # verify text input was received
    
    if(file):
        print("recieved file " + file.filename)
    
    
    # Optional: Save the file to your server. file was already verified to be a pdf on the frontend
    filename = file.filename
    save_path = os.path.join("C:\\Users\\nilay\\Downloads", filename)
    #os.makedirs(os.path.dirname(save_path), exist_ok=True)
    file.save(save_path)
    
    # Process text and file as needed...
    
    return jsonify({'message': 'File and text input received successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
