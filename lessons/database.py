#субд dbms database management system
#sql structured query language язык запросов
import sqlite3

def create_tables(conn):
    #запрос на создание таблицы
    conn.execute("""
    CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, 
    age INTEGER, 
    city TEXT
    )
    """)
def add_users(conn, name, age, city):
    conn.execute('''
    INSERT INTO users(name, age, city)
    VALUES 
    (?, ?, ?)
    ''',
    (name, age, city)
                 )
    conn.commit()
def delete_users():
    ...
