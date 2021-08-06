import mysql.connector

cnx = mysql.connector.connect(user='root', password='jajaveve',
                              host='127.0.0.1',
                              database='store')
#test
mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM orders")

myresult = mycursor.fetchall()

print("test")
for x in myresult:
  print(x)

cnx.close()