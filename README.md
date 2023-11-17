[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/TLLTF7bJ)

#  Second-Hand Goods API

This is an API for managing my store information about my products that are for sale. The API supports two main functionalities: retrieving product details by ID (GET) and adding new products (POST). Additionally, there is a route to get a list of all products.



API Endpoint
1. Get Product by ID
Endpoint: /product/<int:ProductId>
Method: GET
Description: Retrieves product information by ID.
Example: http://127.0.0.1:5000/product/1


2. Add Product
Endpoint: /product
Method: POST
Description: Adds a new product to the database.
Request Body Format: JSON

Example Request: 
{
    "productName": "Smartphone",
    "category": "Electronics",
    "price": 499.99
}

Example Response:
{
    "message": "Product added successfully",
    "id": 3
}

3. Get All Products
Endpoint: /products
Method: GET
Description: Retrieves a list of all products.
Example: http://127.0.0.1:5000/products
