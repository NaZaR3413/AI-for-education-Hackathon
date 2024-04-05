from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/data', methods=['GET'])
def send_data():
    # This could be any data logic; here, we're just sending a simple dictionary
    data = {"message": "Hello from Flask!"}
    return jsonify(data)  # Convert the dictionary to JSON and return it

if __name__ == '__main__':
    app.run(debug=True)
