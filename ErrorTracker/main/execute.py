import cx_Oracle
from classes import Connect, converter
from flask import  Flask, session, url_for, redirect, render_template, request, Markup
'''
We must initialize the flask app first
'''

#Code below will try to connect to database

app=Flask(__name__)
app.config.from_object('config')
login=False

#data=data.reverse() #sends raw data



@app.route("/login/") #all app routes need defining
def FUN_login():
    return render_template("login.html")




#---------------------------------------------------#
@app.route("/")#starting point
def FUN_root():
    #probably need another class to define login credentials
    try:
        app=Flask(__name__)
        session['current_user']="user"
    #Define a SQL query
    except Exception as e:
        print(str(e))


# data=test #needs to refresh to implement table
    return render_template("index.html")#, headers=headers, data=data)






#---------------------------------------------------#
@app.route("/table/")
def FUN_table():
    return render_template("table.html")


@app.route("/public/")
def FUN_public():
   
   
    connector=Connect.attempt()
    conn = cx_Oracle.connect(connector);
    #Get the connection cursor object
    cur = conn.cursor()  # created cursor
    sql = """SELECT * 
        FROM PYTHON_FIRST 
        ORDER BY CALENDAR"""

    cur.execute(sql)
    params = cur.fetchall()
    test1 = converter.printing(params)  # to send to def_home
    data = test1
    bugtitles = []
    descriptions = []
    for i in range(len(data)):
        temp2 = data[i]
        bugtitles.append(temp2[1])
        descriptions.append(temp2[5])
        headers=("Name","Error Title","Contact","Priority","Description","Date","Delete")   
    if session['current_user']=="Admin":
        return render_template("index.html", headers=headers, data=data, bugtitles=bugtitles, descriptions=descriptions)     
    else:
        return render_template("index.html")
   
        


@app.route("/homes/", methods = ["POST"])
def FUN_home():
    errors = []
    #to be edited down
    if 'logged' in request.form: #and (request.form['username'] != 'ab' or request.form['password'] != 'abcd1234'):
        Connect.please(str(request.form['username']),str(request.form['password']))
        user=str(request.form['username'])
        pswrd=str(request.form['password'])
        if converter.find(user,pswrd)==True:
            #connector=Connect.attempt()
            #cx_Oracle.connect(connector);
            session['current_user']="Admin"
            login="True"
            return redirect(url_for('FUN_public'))
      
        else:
            session['current_user']=None
            errors.append("Invalid Login")
            return render_template('login.html', errors=errors)


@app.route("/deleteupdate/")
def FUN_deleteupdate():
        connector=Connect.attempt() #to fix
        conn = cx_Oracle.connect(connector);
        #Get the connection cursor object
        cur=conn.cursor()#created cursor

        firststatement="""update PYTHON_FIRST set ERROR_TITLE = REPLACE(ERROR_TITLE,' ','_')"""
        cur.execute(firststatement)
        conn.commit()
        return redirect(url_for('FUN_public'))
    
    
@app.route("/delete/",methods = ["POST"])
def FUN_delete():
    if 'logged' in request.form:
        connector=Connect.attempt()
        conn = cx_Oracle.connect(connector);
        #Get the connection cursor object
        cur=conn.cursor()#created cursor

        #firststatement="""update PYTHON_FIRST set ERROR_TITLE = REPLACE(ERROR_TITLE,' ','_')"""
        statement = 'delete from PYTHON_FIRST where ERROR_TITLE = :id'
        # cur.execute(firststatement)
        removespace= str(request.form['idnumber'])
        cur.execute(statement, {'id':removespace})
        conn.commit()
    else:
        None
    
      
    return redirect(url_for('FUN_public'))

@app.route("/insert/", methods = ["POST"])
def FUN_insert():
    connector=Connect.attempt()
    conn = cx_Oracle.connect(connector);
    cur=conn.cursor()#created cursor
        #sql_insert="""INSERT INTO PYTHON_FIRST VALUES('bob','Bug Report','7325168926','High','Open','xxxxxxxxxxx', '07/18/21')"""
        #cur.execute(sql_insert)
    if session['current_user']=="Admin":#'submitted' in request.form: #transform back into try catch
    # sql_insert="""INSERT INTO PYTHON_FIRST VALUES('bob','Bug Report','7325168926','High','xxxxxxxxxxx', '07/18/21')"""
    # cur.execute(sql_insert)
        data={'1':str(request.form['Named']),'2':str(request.form['Error_title']),'3':str(request.form['Contact']),'4':str(request.form['Priority']),'5':str(request.form['Description']),'6':str(request.form['Date'])}
        statements = """INSERT INTO PYTHON_FIRST VALUES(:1,:2,:3,:4,:5,:6)"""
        cur.execute(statements,data) #THE PROBLEM CHILD
    #   print('Insert Completed')
        conn.commit()
      
    else:
        None   
    cur.close()
    conn.close()#might 
    #cur.close()
    # conn.close()
    return redirect(url_for('FUN_deleteupdate'))
    
        


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",use_reloader=False) #this hosts temporarily on local link provided







              
