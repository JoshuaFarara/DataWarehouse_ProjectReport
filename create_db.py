import mysql.connector

mydb = mysql.connector.connect(host='localhost',
    user='root',
    password='1038368', 
    passwd='1038368'
    )


my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE my_datawarehouse")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)