from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample order data
orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    order = request.get_json()
    orders.append(order)
    return jsonify({"message": "Order created", "order": order})

@app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)