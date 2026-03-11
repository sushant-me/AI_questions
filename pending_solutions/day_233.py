""" Connect Python to MySQL database. """

import mysql.connector

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="https://example.com",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function to test the connection
connect_to_mysql()