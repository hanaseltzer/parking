import mysql.connector
from mysql.connector import Error
import os


host = os.getenv('mysql_host')
user = os.getenv('mysql_user')
password = os.getenv('mysql_password')

def create_database(db_name):
    manage_database('create', db_name)

def delete_database(db_name):
    manage_database('delete', db_name)

def manage_database(action, db_name):
    try:
        # Establish connection to the MySQL server
        connection = mysql.connector.connect(
            host=host, user=user, password=password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create a new database
            if action == 'delete':
                cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
                print(f"Database {db_name} deleted successfully!")
            elif action == 'create':
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"Database {db_name} created successfully!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function

