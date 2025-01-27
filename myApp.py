from flask import Flask
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "ShAmp00x!",
    database= "expensesregister"
)

mycursor = db.cursor()

@app.get("/new-expense")
def hello_world():
    return "<p>Hello World</p>"

#Get all current entries in our db
@app.get("/all-expenses")
def all_entries():
    mycursor.execute("SELECT * FROM dailyexpenses")
    results = mycursor.fetchall()  # Fetch all rows from the executed query
    if not results:
        return "<p> Waiting for your first entry! <p>"
    else: 
        return "<br>".join(str(row) for row in results)  # Join all rows with line breaks
