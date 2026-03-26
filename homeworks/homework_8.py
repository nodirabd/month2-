import sqlite3


def setup_db(conn):
    # для удаления таблицы каждый раз при запуске
    conn.execute('DROP TABLE IF EXISTS books')

    conn.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')

    books = [

        ('Белый пароход', 'Чынгыз Айтматов', 1970, 'Повесть', 192, 5),
        ('Кыямат', 'Чынгыз Айтматов', 1986, 'Роман', 450, 10),
        ('Дюна', 'Фрэнк Герберт', 1965, 'Фантастика', 700, 4),
        ('Цветы для Элджернона', 'Дэниел Киз', 1966, 'Драма', 320, 6),
        ('Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Классика', 480, 5),
        ('Норвежский лес', 'Харуки Мураками', 1987, 'Роман', 380, 3),
        ('Краткие ответы на большие вопросы', 'Стивен Хокинг', 2018, 'Наука', 256, 8),
        ('Портрет Дориана Грея', 'Оскар Уайльд', 1890, 'Классика', 320, 4),
        ('Алхимик', 'Пауло Коэльо', 1988, 'Притча', 208, 9)
    ]
    conn.executemany(
        'INSERT INTO books ('
        'name, author, publication_year, '
        'genre, number_of_pages, number_of_copies)'
        ' VALUES (?, ?, ?, ?, ?, ?)',
        books)
    conn.commit()


def get_books_by_author(conn, author):
    cursor = conn.execute('SELECT name FROM books WHERE author = ? '
                          'ORDER BY name ASC', (author,))
    return cursor.fetchall()


conn = sqlite3.connect("homework_8.db")
setup_db(conn)  # Теперь таблица будет обновляться при каждом запуске

author = "Чынгыз Айтматов"
print(f"Список книг {author}:")
for row in get_books_by_author(conn, author):
    print(f"- {row[0]}")

conn.close()