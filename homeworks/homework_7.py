import sqlite3


def create_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')
    conn.commit()


def insert_books(conn, books_list):# executemany используме если много данных
    conn.executemany('''         
        INSERT INTO books (name, author, publication_year, 
        genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', books_list)
    conn.commit()


if __name__ == "__main__":
    connection = sqlite3.connect('homework_7.db')

    books_to_add = [
        ('Кыямат', 'Чынгыз Айтматов', 1986, 'Роман', 450, 10),
        ('Sapiens', 'Юваль Ной Харари', 2011, 'Научпоп', 520, 7),
        ('Дюна', 'Фрэнк Герберт', 1965, 'Фантастика', 700, 4),
        ('Цветы для Элджернона', 'Дэниел Киз', 1966, 'Драма', 320, 6),
        ('Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Классика', 480, 5),
        ('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 12),
        ('Норвежский лес', 'Харуки Мураками', 1987, 'Роман', 380, 3),
        ('Краткие ответы на большие вопросы', 'Стивен Хокинг', 2018, 'Наука', 256, 8),
        ('Портрет Дориана Грея', 'Оскар Уайльд', 1890, 'Классика', 320, 4),
        ('Алхимик', 'Пауло Коэльо', 1988, 'Притча', 208, 9)
    ]


print("База данных успешно обновлена. Добавлено 10 книг.")
