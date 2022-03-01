from flask import request,Flask,render_template
import sqlite3

app=Flask(__name__)

db='practice.db'

@app.route("/",methods=["GET","POST"])
def main_matter():
    if request.method=="GET":
        return render_template('login_main.html',fail='')
    else:
        creds=(
            request.form['username'],
            request.form['password']
        )
        result=check(creds)
        if(result!=None):
            return success(result[2])
        return render_template('login_main.html',fail='Invalid Username or password!')


def check(creds):
    connection_route=sqlite3.connect(db)
    cursor=connection_route.cursor()
    req=cursor.execute('SELECT * from Credentials where username=? and password=?',creds).fetchone()
    connection_route.close()
    return req

def success(result):
    return render_template('login_success.htm',name=result)