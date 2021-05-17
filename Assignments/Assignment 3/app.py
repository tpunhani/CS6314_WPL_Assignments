from flask import Flask, render_template, request, json, redirect
from flaskext.mysql import MySQL
from flask import session


app = Flask(__name__)

mysql = MySQL()

# MYSQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'todolist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)


app.secret_key = 'secret-key'


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template("signup.html")


@app.route('/signUp', methods=['POST'])
def signUp():

    # read the posted value from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tbl_user(name, email, password) VALUES (%s, %s, %s)", (_name, _email, _password))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully!'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span> Enter the required fields! </span>'})


@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')


@app.route('/showAddItem')
def showAddItem():
    return render_template('addItem.html')


@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tbl_user WHERE email = %s", (_email))

        data = cursor.fetchall()

        if len(data) > 0:
            if str(data[0][3]) == _password:
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html', error='Wrong Email address or password entered!')

        else:
            return render_template('error.html', error='Wrong Email address or password entered!')

    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/addItem', methods=['POST'])
def addItem():
    try:
        if session.get('user'):
            _title = request.form['inputTitle']
            _description = request.form['inputDescription']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO tbl_todo(title, description, userid) VALUES (%s, %s, %s)", (_title, _description, _user))

            data = cursor.fetchall()

            if len(data) == 0:
                conn.commit()
                return redirect('/userHome')

            else:
                return render_template('error.html', error='An error occurred while adding an element in todo list')

        else:
            return render_template('error.html', error='Unauthorized access')

    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error='Unauthorized access')


@app.route('/listing', methods=['GET'])
def listing():
    try:
        if session.get('user'):
            _user = session.get('user')
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tbl_todo WHERE userid = %s", (_user))
            # this will extract row headers
            row_headers = [x[0] for x in cursor.description]
            data = cursor.fetchall()
            json_data = []
            if len(data) > 0:
                for result in data:
                    json_data.append(dict(zip(row_headers, result)))
            return json.dumps(json_data)

        else:
            return render_template('error.html', error='Unauthorized access')

    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/editItem')
def editItem():
    try:
        if session.get('user'):
            _user = session.get('user')
            _id = request.args['id']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT title, description, isComplete FROM tbl_todo WHERE userid=%s AND id=%s", (_user, _id))
            data = cursor.fetchall()
            if len(data) > 0:
                conn.commit()
                return render_template('editItem.html', title=data[0][0], description=data[0][1], status=data[0][2], id=_id)
        else:
            return render_template('error.html', error='Unauthorized access')

    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/updateItem', methods=['POST'])
def updateItem():
    try:
        if session.get('user'):
            _user = session.get('user')
            _title = request.form['inputTitle']
            _description = request.form['inputDescription']
            _id = request.args['id']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE tbl_todo SET title=%s, description=%s WHERE userid=%s AND id=%s",
                           (_title, _description, _user, _id))
            conn.commit()
            return redirect('/userHome')
        else:
            return render_template('error.html', error='Unauthorized access')

    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/deleteItem')
def deleteItem():
    try:
        if session.get('user'):
            _user = session.get('user')
            _id = request.args['id']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM tbl_todo WHERE userid=%s AND id=%s", (_user, _id))
            conn.commit()
            return redirect('/userHome')
        else:
            return render_template('error.html', error='Unauthorized access')

    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/changeStatus', methods=['POST'])
def changeStatus():
    try:
        if session.get('user'):
            _user = session.get('user')
            _id = request.args['id']
            _rem_status = request.args['status']
            _status = True
            if _rem_status != '0':
                _status = False
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tbl_todo SET isComplete=%s WHERE userid=%s AND id=%s", (_status, _user, _id))
            conn.commit()
            return redirect('/userHome')
        else:
            return render_template('error.html', error='Unauthorized access')

    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == "__main__":
    app.run()
