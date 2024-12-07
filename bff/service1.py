from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def get_users():
    # Simulated user data
    return jsonify({"id": 1, "name": "John Doe", "email": "john.doe@example.com"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
