import mysql.connector
import datetime
import random
from sql_connection import get_sql_connection


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
    #test
    mycursor = cnx.cursor()
    query1 = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products inner join uom on products.uom_id = uom.uom_id"
    mycursor.execute(query1)
    myresult = mycursor.fetchall()
    print(myresult)
    #select items so the min-criteria is met
    total = 0
    while total < min_total:
        item = random.choice(myresult)
        print(item)
        total += item[3]
    print(total)
    #create order entry in order TABLE
    qu = "INSERT INTO orders(customer_id, total, datetime) VALUES(%s, %s, %s)"
    order_time  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    s = (random.randint(1,11), total, order_time)
    print(s)
    mycursor.execute(qu,s)
    connection.commit()
    #add orders to the order_details table
    #add total_amount to order table
    cnx.close()
if __name__ == '__main__':
    connection = get_sql_connection()
    dict_ = {'product_name': 'premium potato', 'uom_id': '1', 'price_per_unit': 100}
    #insert_new_product(connection, dict_)
    #delete_product(connection,  [i for i in range(20,49)])
    #get_all_products(connection)
    print(type(connection))
    update_product(connection, 46, 10000)
    create_random_order(connection, 100)