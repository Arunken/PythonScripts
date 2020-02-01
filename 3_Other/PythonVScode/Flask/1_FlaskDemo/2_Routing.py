from flask import Flask
import sqlite3 as sql

app = Flask(__name__)

# routing 
@app.route("/")
def hello():
    print("hello called")
    return "Hello World!"

''' or add url rule using add_url_rule function

def hello_world():
   return ‘hello world’
app.add_url_rule(‘/’, ‘hello’, hello_world)

'''

# accepting a string value 
@app.route("/addname/<name>")
def acceptName(name):
    print("add name called")
    return "Hello %s"%name

# accepting an int
@app.route("/addage/<int:age>")
def acceptAge(age):
    print("add age called")
    return "Age :%d"%age

# accepting a float
@app.route("/addtemp/<float:temp>")
def accepttemp(temp):
    print("add temp called")
    return "Temperature %f"%temp

if __name__ == "__main__":
    app.run(debug=True) #By default it runs on localhost
    #app.run(host="127.0.0.1",port="4444",debug=True) # custom server address
    #app.run(host= '0.0.0.0') # to run on your machines IP address and open it to non-local connections