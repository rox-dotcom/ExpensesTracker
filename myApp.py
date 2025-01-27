from dotenv import load_dotenv
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

load_dotenv()

# Access the variables
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

db = mysql.connector.connect(
    host= os.getenv("DB_HOST"),
    user= os.getenv("DB_USER"),
    password= os.getenv("DB_PASSWORD"),
    database= os.getenv("DB_NAME")
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
