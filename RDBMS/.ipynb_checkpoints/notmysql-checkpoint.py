# import mysql.connector
# from datetime import datetime

# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='1038368', #change this for your specific server
#     database="datawarehouse" # connect to specific database
# )
# Create database
# mycursor.execute("CREATE DATABASE testdatabase")
# mycursor = db.cursor()

''' create a table'''
# mycursor.execute("CREATE TABLE Client (name VARCHAR(50), age smallint UNSIGNED, clientID int PRIMARY KEY AUTO_INCREMENT)")

# display the contents of the table
# mycursor.execute("DESCRIBE Client")

# for x in mycursor:
#     print(x)

'''Inserting Items into table'''
# mycursor.execute("INSERT INTO Client (name, age) VALUES (%s,%s)", ("Caleb", 29))
# commit changes to database
# db.commit()

# mycursor.execute("SELECT * FROM Client")

# for x in mycursor:
#     print(x)

'''create another table'''
# mycursor.execute("CREATE TABLE Haircut (name varchar(50) NOT NULL, appointment datetime NOT NULL, hairstyle ENUM('FullHaircut', 'LineUp', 'Beard') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

# Insert items into table
# mycursor.execute("INSERT INTO Haircut (name, appointment, hairstyle) VALUES (%s,%s,%s)", ("Blend", datetime.now(), "FullHaircut"))
# db.commit()

'''Display some elements from the table'''
# mycursor.execute("SELECT id,  FROM Haircut WHERE hairstyle = 'FullHaircut' ORDER BY id DESC")

# for x in mycursor:
#     print(x)