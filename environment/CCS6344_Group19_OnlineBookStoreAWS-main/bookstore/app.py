from flask import Flask, render_template, request, redirect, url_for
import pymysql


app = Flask(__name__)

# Database connection details
endpoint = "obs-database.c4v5xzujhxv5.us-east-1.rds.amazonaws.com"
port = 3306
dbname = "mydb"
username = "admin"
password = "Pa$$w0rd123"

def get_db_connection():
    return pymysql.connect(
        host=endpoint,
        user=username,
        password=password,
        database=dbname,
        port=port
    )
#Index Route(displays a list of books fetched from the MySQL)
@app.route('/')
def index():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM book")
            books = cursor.fetchall()
    finally:
        connection.close()
    return render_template('index.html', books=books)

#Add Book Route
@app.route('/add', methods=['POST'])
def add_book():
    name = request.form['name']
    price = request.form['price']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO book (name, price) VALUES (%s, %s)", (name, price))
            connection.commit()
    finally:
        connection.close()
    return redirect(url_for('index'))

#Delete Book Route
@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM book WHERE id = %s", (id,))
            connection.commit()
    finally:
        connection.close()
    return redirect(url_for('index'))

#Connect to Web Server with port 3000
if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
