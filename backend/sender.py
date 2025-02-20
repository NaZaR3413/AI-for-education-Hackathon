from flask import Flask, jsonify
from flask_cors import CORS
#from coder import query
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/data', methods=['GET'])
def send_data():
    # Send a list of numbers instead of a message
    numbers = [4, 77.39382051057605, 70.55662101758571, 69.02663978818158, 63.10514303296857]
    #numbers = query()
    #return jsonify(query())  # Directly returning the list as JSON
    return jsonify(numbers)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)
