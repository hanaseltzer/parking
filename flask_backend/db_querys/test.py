import mysql.connector

a = mysql.connector.connect(
                host='35.224.216.57',
                user='root',
                password='parkthatcar000',
                database='org1'
            )
print(a)