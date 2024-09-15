import mysql.connector
from mysql.connector import Error
import os

class DatabaseManager:
    def __init__(self, host, user, password, database):
        """Initialize the database connection parameters."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        """Enter the runtime context related to this object."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object."""
        self.disconnect()

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

    def execute(self, query, commit=False, fetch=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            if fetch == 'all':
                result = cursor.fetchall()
                return result
            elif fetch == 'one':
                result = cursor.fetchone()
                return result
            if commit:
                self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def create_table(self, table_name, columns):
            
        # Build the CREATE TABLE query
        column_definitions = ", ".join([f"{name} {type_}" for name, type_ in columns.items()])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
        self.execute(create_table_query)
        # print(f"Table `{table_name}` created successfully")

    def create_row(self, table_name, data):
        try:
            cursor = self.connection.cursor()
            
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            
            cursor.execute(insert_query, tuple(data.values()))
            self.connection.commit()
            print("Row added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def get_row(self, table_name, conditions=None):
        try:
            cursor = self.connection.cursor()
            if conditions:
                condition_statements = " AND ".join([f"{column} = %s" for column in conditions.keys()])
            select_query = f"SELECT * FROM {table_name}"
            if conditions:
                select_query = f"{select_query} WHERE {condition_statements}"
            
            cursor.execute(select_query, tuple(conditions.values()))
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def get_rows(self, table_name, conditions=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            if conditions:
                condition_statements = " AND ".join([f"{column} = %s" for column in conditions.keys()])
            select_query = f"SELECT * FROM {table_name}"
            if conditions:
                select_query = f"{select_query} WHERE {condition_statements}"
                cursor.execute(select_query, tuple(conditions.values()))
            else:
                cursor.execute(select_query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    # def create_database():
    #     query = 

host = os.getenv('mysql_host')
user = os.getenv('mysql_user')
password = os.getenv('mysql_password')

def mysql_decorator(func):
    def wrapper(*args, **kwargs):
        with DatabaseManager(host=host, user=user, password=password, database='org1') as db:
            return func(db, *args, **kwargs)
    return wrapper

