from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/orders', methods=['GET'])
def get_orders():
    # Simulated order data
    return jsonify([
        {"order_id": 101, "product": "Laptop", "quantity": 1},
        {"order_id": 102, "product": "Mouse", "quantity": 2}
    ]), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
