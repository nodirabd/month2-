from lessons.lesson_5 import Money
from lessons.database import (
    create_tables,
    add_users,
    delete_users)
import sqlite3

money_1 =Money(10, 'USD')
connection =sqlite3.connect('database.db')
create_tables(connection)
add_users(
    connection,
    'Nodira', 18, 'Bishkek',
         )
