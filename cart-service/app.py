from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample cart data
cart = []

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

@app.route('/cart', methods=['POST'])
def add_to_cart():
    item = request.get_json()
    cart.append(item)
    return jsonify({"message": "Item added to cart", "cart": cart})

@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    global cart
    cart = [item for item in cart if item['id'] != item_id]
    return jsonify({"message": "Item removed from cart", "cart": cart})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)