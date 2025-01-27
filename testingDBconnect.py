import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "ShAmp00x!",
    database= "expensesregister"
)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE ExpensesRegister")

#mycursor.execute("SHOW DATABASES")

#mycursor.execute("CREATE TABLE dailyexpenses (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), category VARCHAR(255), amount FLOAT, date DATE)")

mycursor.execute("SELECT * FROM dailyexpenses")
results = mycursor.fetchall()  # Fetch all rows from the executed query
for row in results:
    print(row) 

print(results)