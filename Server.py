from flask import Flask, request, jsonify
import pymysql
from datetime import datetime

app = Flask(__name__)

# Connect to the MySQL database
connection = pymysql.connect(
    host='mysql.s458.sureserver.com',
    port=3306,
    user='moti2',
    password='devops1234',
    db='msdeal_devops'
)

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'POST':
        # Get the data from the HTML form
        name = request.form.get('name')
        age = request.form.get('age')
        date_created = datetime.now()

        # Validate the input
        if not name:
            return jsonify({'status': 'error', 'message': 'Name is required'})
        if not age:
            return jsonify({'status': 'error', 'message': 'Age is required'})

        try:
            with connection.cursor() as cursor:
                # Insert the data into the 'users' table
                sql = "INSERT INTO users (name, age, date_created) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, age, date_created))
                connection.commit()

            return jsonify({'status': 'success'})
        except pymysql.Error as e:
            return jsonify({'status': 'error', 'message': str(e)})

    elif request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                # Retrieve all the data from the 'users' table
                sql = "SELECT * FROM users"
                cursor.execute(sql)
                result = cursor.fetchall()
                return jsonify(result)
        except pymysql.Error as e:
            return jsonify({'status': 'error', 'message': str(e)})

    elif request.method == 'PUT':
        # Get the data from the HTML form
        name = request.form.get('name')
        age = request.form.get('age')

        # Validate the input
        if not name:
            return jsonify({'status': 'error', 'message': 'Name is required'})
        if not age:
            return jsonify({'status': 'error', 'message': 'Age is required'})

        try:
            with connection.cursor() as cursor:
                # Update the data in the 'users' table
                sql = "UPDATE users SET age = %s WHERE name = %s"
                cursor.execute(sql, (age, name))
                connection.commit()
            return jsonify({'status': 'success'})
        except pymysql.Error as e:
            return jsonify({'status': 'error', 'message': str(e)})

    elif request.method == 'DELETE':
        # Get the data from the HTML form
        name = request.form.get('name')

        # Validate the input
        if not name:
            return jsonify({'status': 'error', 'message': 'Name is required'})

        try:
            with connection.cursor() as cursor:
                # Delete the data from the 'users' table
                sql = "DELETE FROM users WHERE name = %s"
                cursor.execute(sql, (name))
                connection.commit()
            return jsonify({'status': 'success'})
        except pymysql.Error as e:
            return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run()
