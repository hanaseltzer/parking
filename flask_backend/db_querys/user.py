from db_querys.db import mysql_decorator

@mysql_decorator
def create_user(db_conn, user_data):
    db_conn.create_row('users', user_data)

@mysql_decorator
def get_user(db_conn, username):
    conditions = {'username': username}
    result = db_conn.get_rows('users', conditions)
    return result

@mysql_decorator
def get_users(db_conn):
    users = db_conn.get_rows('users')
    for user in users:
        user["created_at"] = user["created_at"].isoformat()
        conditions = {'user_id': user["id"]}
        parking_spots = db_conn.get_rows('parkingSpots', conditions)
        if parking_spots:
            user["parking_spots"] = True
        else:
            user["parking_spots"] = False
    return users

# create_user({
#     'username': 'dudi',
#     'full_name': 'david shoshany'
#     'password': 'abc123',
#     'phone_number': '0547666054',
# })


# a = get_users()
# print(a)