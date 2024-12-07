from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# BFF endpoint to aggregate data
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Fetch data from microservices
        user_service = requests.get('http://localhost:5001/users').json()
        order_service = requests.get('http://localhost:5002/orders').json()

        # Combine data from both services
        response = {
            "user": user_service,
            "orders": order_service
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
