
from flask import Flask, render_template, request,session,redirect,url_for

app = Flask(__name__)
#app.config['SESSION_TYPE'] = 'memcached'
#app.config['SECRET_KEY'] = 'super secret key'
app.secret_key = 'kenrigx999'


@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
   return  "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"


@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template("login.html")

   
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))


if __name__ =='__main__':
    app.run(debug=True)