from flask import Flask
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def hello():
    print("hello called")
    return "Hello World!"

if __name__ == "__main__":
    app.run()