import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customers")
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# myresult = mycursor.fetchone()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

