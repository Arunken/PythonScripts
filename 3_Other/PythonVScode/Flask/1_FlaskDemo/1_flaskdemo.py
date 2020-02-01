from flask import Flask
import sqlite3 as sql

app = Flask(__name__)

# routing 
@app.route("/")
def hello():
    print("hello called")
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True) #By default it runs on localhost
    #app.run(host="127.0.0.1",port="4444",debug=True) # custom server address
    #app.run(host= '0.0.0.0') # to run on your machines IP address and open it to non-local connections