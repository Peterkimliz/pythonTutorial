import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="kimani89",database="laravel")
mycursor=mydb.cursor()
mycursor.execute("select * from categories ORDER BY name asc")

for i in mycursor:
    print(i)