import mysql.connector

cnx = mysql.connector.connect(user='root', password='jajaveve',
                              host='127.0.0.1',
                              database='store')
#test
mycursor = cnx.cursor()

mycursor.execute("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit FROM products inner join uom on products.uom_id = uom.uom_id")

myresult = mycursor.fetchall()

print("test")
for x in myresult:
  print(x)

cnx.close()