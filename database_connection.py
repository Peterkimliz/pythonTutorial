import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="kimani89",database="python")
mycursor=mydb.cursor()
mycursor.execute("show tables")

for i in mycursor:
    print(i)