import mysql. connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="ajmal1121",
    database="id"
)
#LIMIT
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students LIMIT 4")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
