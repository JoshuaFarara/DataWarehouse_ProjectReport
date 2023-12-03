from sqlalchemy import create_engine
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1038368"
    )
    print("Connection established")
    cursor = mydb.cursor()
    cursor.execute("create database if not exists datawarehouse")
    mydb.commit()
    print("Database created successfully")
    cursor.execute("use datawarehouse")

except mysql.connector.Error as err:
    print("An error occurred:", err)

database = 'datawarehouse'
hostname = 'localhost'
username = 'root'
password = '10388368'

# engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))
engine = create_engine("mysql+mysqldb://root:1038368@localhost/datawarehouse")