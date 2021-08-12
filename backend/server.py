#flask lightweight
from flask import Flask, jsonify, request, render_template
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

#defines an endpoint

"""
@app.route("/")
def index():
    return render_template("index.html", my_string= "unit", my_list = tuple(products))
"""

#run an endpoint
@app.route('/hello')
def hello():
    return "Hello, how are you dude?"

@app.route('/your_flask_funtion')
def your_flask_funtion():
 	render_template("index.html", my_string= "unit", my_list = tuple(products))

@app.route('/get_products', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    print(products)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def student():
   return render_template('enternewproduct.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      for i,j in result.items():
          print(i,j)
      #print(result.get_json())
      name = request.form['Name']
      uo= request.form['uom_id']
      pri = request.form['price_per_unit']
      dict_ = {'product_name': name, 'uom_id': uo, 'price_per_unit': pri}
      products_dao.insert_new_product(connection, dict_)

      #Update the item entries in items-table
      products = products_dao.get_all_products(connection)
      print(tuple(products))
      return render_template("index.html", my_string= "unit", my_list = tuple(products))
      #return render_template("result.html",result = result)

if __name__ == "__main__":
    print("Starting Python Flask Server For Store Management System")
    app.run(port=5000)
    app.run(debug=True)