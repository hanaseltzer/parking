from db import mysql_decorator
from db_mgmt import create_database, delete_database
import json

@mysql_decorator
def create_user_table(db_conn):
    table_name = 'users'
    columns = {
        'id': 'INT AUTO_INCREMENT PRIMARY KEY',
        'username': 'VARCHAR(50) NOT NULL UNIQUE',
        'password': 'VARCHAR(255) NOT NULL',
        'phone_number': 'VARCHAR(20)',
        'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
    }
    db_conn.create_table(table_name, columns)

@mysql_decorator
def create_floors_table(db_conn):
    table_name = 'floors'
    columns = {
        'floor_id': 'INT AUTO_INCREMENT PRIMARY KEY',
        'floor_name': 'VARCHAR(100) NOT NULL'
    }
    db_conn.create_table(table_name, columns)

@mysql_decorator
def create_ParkingSpots_table(db_conn):
    table_name = 'parkingSpots'
    columns = {
        'spot_id': 'INT AUTO_INCREMENT PRIMARY KEY',
        'spot_name': 'VARCHAR(100) NOT NULL',
        'x_coord': 'INT NOT NULL',
        'y_coord': 'INT NOT NULL',
        'user_id': 'INT',
        'available': 'BOOLEAN DEFAULT TRUE',
        'floor_id': 'INT',
        'FOREIGN': 'KEY (floor_id) REFERENCES Floors(floor_id)'
    }
    db_conn.create_table(table_name, columns)


tables_schema_path = 'flask_backend\\db_querys\\tables_schema.json'
@mysql_decorator
def create_tables(db_conn):
    with open(tables_schema_path, 'r') as f:
        tables = json.load(f)
    for table in tables:
        db_conn.create_table(table["table_name"], table["columns"])

def create_org(org_name):
    create_database(org_name)
    create_tables()

delete_database('org1')
create_org('org1')