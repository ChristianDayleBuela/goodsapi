from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "productName": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "productName": "Book", "category": "Books", "price": 19.99},
]
@app.route('/product/<int:ProductId>', methods=['GET'])
def GetProduct(ProductId):
    product = next((p for p in products if p['id'] == ProductId), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404



