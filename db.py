import mysql.connector
import settings

connection = mysql.connector.connect(
    user=settings.user,
    password=settings.password,
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS users_db")
cursor.execute("USE users_db")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id int auto_increment primary key, 
    name varchar(64) not null, 
    username varchar(64) not null, 
    password varchar(255) not null
);""")

def get_user(username):
    cursor.execute("select * from users where username=%s", (username, ))
    
    user = cursor.fetchone()
    if user:
        return user

    return None

def enter_infos(name, username, password):
    cursor.execute("insert into users (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
    connection.commit()
    