import mysql.connector, settings

connection = mysql.connector.connect(
    user=settings.user,
    password=settings.password,
)

cursor = connection.cursor()
cursor._executed("create database if not exists UsersDB")
cursor.execute("use UsersDB")

def create_table():
    cursor.execute("create table if not exists User_infos (id auto_increment primary key, name varchar(64) not null, username varchar(64) not null, password varchar(256) not null)")

def enter_infos(name, username, password):
    cursor.execute("insert into UserDB VALUES (%s, %s, %s)"(name, username, password))