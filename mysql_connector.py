import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="py@162200"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM CUSTOMER")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)

