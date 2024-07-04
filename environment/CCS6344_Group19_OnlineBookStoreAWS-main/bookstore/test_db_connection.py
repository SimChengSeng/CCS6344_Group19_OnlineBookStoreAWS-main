import pymysql

# Database connection details
endpoint = "obs-database.c4v5xzujhxv5.us-east-1.rds.amazonaws.com"
port = 3306
dbname = "mydb"  # Updated database name
username = "admin"
password = "Pa$$w0rd123"

connection = None

try:
    # Connect to the database
    connection = pymysql.connect(
        host=endpoint,
        user=username,
        password=password,
        database=dbname,
        port=port
    )

    with connection.cursor() as cursor:
        # Execute a query
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        print("Database version:", result)
except pymysql.MySQLError as e:
    print(f"Error connecting to the database: {e}")
finally:
    if connection:
        connection.close()
