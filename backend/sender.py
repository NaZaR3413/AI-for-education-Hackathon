from flask import Flask, jsonify
from flask_cors import CORS
from code import scores_calc
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/data', methods=['GET'])
def send_data():
    # Send a list of numbers instead of a message
    #numbers = [4, 77.39382051057605, 70.55662101758571, 69.02663978818158, 63.10514303296857]
    numbers = scores_calc
    return jsonify(numbers)  # Directly returning the list as JSON

if __name__ == '__main__':
    app.run(debug=True)
