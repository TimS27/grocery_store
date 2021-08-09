from flask import Flask, jsonify, request
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

# @app.route('/hello')
# def hello():
#    return "Hello, how are you dude?"


@app.route('/get_products', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    print(products)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Store Management System")
    app.run(port=5000)
