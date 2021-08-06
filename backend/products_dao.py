import mysql.connector

cnx = mysql.connector.connect(user='root', password='password1',
                              host='127.0.0.1',

                              database='store')

cursor = cnx.cursor()   #cursor will hold data from sql query

query = "SELECT * FROM store.products;"

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit) in cursor:
    print(product_id, name, uom_id, price_per_unit)

cnx.close()

#test comment