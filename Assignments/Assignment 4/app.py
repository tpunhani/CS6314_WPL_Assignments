from flask import Flask, render_template, request, json, redirect
from flaskext.mysql import MySQL
from flask import jsonify


app = Flask(__name__)

mysql = MySQL()

# MYSQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'FavoritePlaces'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)


@app.route("/")
def main():
    return render_template('google-maps.html')


@app.route('/favplaces', methods=['GET'])
def listing():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Restaurants")
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        data = cursor.fetchall()
        json_data = []
        if len(data)>0:
            for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)

    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == "__main__":
    app.run()