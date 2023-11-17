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

@app.route('/product', methods=['POST'])
def AddProduct():
    data = request.get_json()

    RequiredFields = ['productName', 'category', 'price']
    if not all(field in data for field in RequiredFields):
        return jsonify({"message": "Missing required fields"}), 400

    NewId = max([p['id'] for p in products]) + 1 if products else 1

    NewProduct = {
        "id": NewId,
        "productName": data['productName'],
        "category": data['category'],
        "price": data['price'],
    }

    products.append(NewProduct)

    return jsonify({"message": "Product added successfully", "id": NewId}), 201


