import sqlite3

def create_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')
    conn.commit()

def insert_books(conn, books_list):
    conn.executemany('''         
        INSERT INTO books (name, author, publication_year,
        genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', books_list)
    conn.commit()