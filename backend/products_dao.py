import mysql.connector
import datetime
import random
from sql_connection import get_sql_connection
import numpy as np
import pandas as pd

def get_all_products(cnx):
    cnx.reconnect()
    mycursor = cnx.cursor()
    query1 = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products inner join uom on products.uom_id = uom.uom_id"
    mycursor.execute(query1)
    myresult = mycursor.fetchall()

    response = []

    #print("query")
    for x in myresult:
        response.append(x)
        #print(x)
    cnx.close()
    return response


def insert_new_product(cnx, dict_):
    cnx.reconnect()
    mycursor = cnx.cursor()
    query2 = ("INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s,%s,%s)")
    data = (dict_['product_name'], dict_['uom_id'], dict_['price_per_unit'])
    q = query2 % data
    print(q)
    mycursor.execute(query2, data)
    # Commits Database Change
    cnx.commit()
    myresult = mycursor.fetchall()

    print("inserted")
    for x in myresult:
        print(x)
    cnx.close()

def delete_product(cnx, product_ids):
    cnx.reconnect()
    #The MySQLCursor class instantiates objects that can execute operations such as SQL statements.
    cursor = cnx.cursor()
    for product_id in product_ids:
        query = ("DELETE FROM products where product_id=" +str(product_id))
        cursor.execute(query)
        connection.commit()
        print("deleted")
    cnx.close()

def update_product(cnx, product_id, changed_price):
    cnx.reconnect()
    #The MySQLCursor class instantiates objects that can execute operations such as SQL statements.
    cursor = cnx.cursor()

    sql = "UPDATE products SET price_per_unit = %s WHERE product_id = %s"
    val = (str(changed_price), str(product_id))
    cursor.execute(sql,val)
    connection.commit()
    print("deleted")
    cnx.close()

def create_random_order(cnx, min_total):
    #get all items which are in the database
    cnx.reconnect()
    mycursor = cnx.cursor()
    query1 = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products inner join uom on products.uom_id = uom.uom_id"
    mycursor.execute(query1)
    available_products = mycursor.fetchall()
    print(available_products)

    id_price={}
    for p in available_products:
        id_price[p[0]] = p[3]
    #print(id_price)

    #select items so the min-criteria is met
    total = 0
    selected_products = []
    while total < min_total:
        item = random.choice(available_products)

        total += item[3]
        selected_products.append(item[0])

    #create order entry in order TABLE
    qu = "INSERT INTO orders(customer_id, total, datetime) VALUES(%s, %s, %s)"
    order_time  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    customer_id = random.randint(1,11)
    s = (customer_id, total, order_time)
    #print(s)
    mycursor.execute(qu,s)
    connection.commit()

    qu2 = "SELECT order_id from orders ORDER BY order_id DESC Limit 1"
    mycursor.execute(qu2)
    myres = mycursor.fetchall()

    order_id = myres[0][0]

    #add orders to the order_details table
    #add total_amount to order table

    x = pd.value_counts(selected_products)
    for product_id, quantity in x.items():
        print(product_id, quantity)
        que = "INSERT INTO order_details(order_id, product_id, quantity, total_price) VALUES(%s, %s, %s, %s)"
        data = (order_id, product_id, quantity, quantity*id_price[product_id])
        mycursor.execute(que, data)
        connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    dict_ = {'product_name': 'premium potato', 'uom_id': '1', 'price_per_unit': 100}
    #insert_new_product(connection, dict_)
    #delete_product(connection,  [i for i in range(20,49)])
    #get_all_products(connection)
    print(type(connection))
    update_product(connection, 46, 10000)
    create_random_order(connection, 100)