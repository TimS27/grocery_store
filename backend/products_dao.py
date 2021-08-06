import mysql.connector
from sql_connection import get_sql_connection
def get_all_products(cnx):
    cnx.reconnect()
    #test
    mycursor = cnx.cursor()
    query1 = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products inner join uom on products.uom_id = uom.uom_id"
    mycursor.execute(query1)
    myresult = mycursor.fetchall()

    print("query")
    for x in myresult:
      print(x)
    cnx.close()

def insert_new_product(cnx, dict_):
    cnx.reconnect()
    mycursor = cnx.cursor()
    query2 = ("INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s,%s,%s)")
    data =(dict_['product_name'],dict_['uom_id'], dict_['price_per_unit'])
    q= query2 % data
    print(q)
    mycursor.execute(query2, data)
    # Commits Database Change
    cnx.commit()
    myresult = mycursor.fetchall()

    print("inserted")
    for x in myresult:
      print(x)
    cnx.close()


if __name__ == '__main__':
    connection = get_sql_connection()


    dict_ = {'product_name': 'potato', 'uom_id': '1', 'price_per_unit': 10}
    insert_new_product(connection, dict_)

    get_all_products(connection)