import sqlite3
import os


def database_entry(name, column, value):
    base_path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_path, 'reg_base.sqlite')
    database = sqlite3.connect(db_path)
    cursor = database.cursor()

    if name and column and value:
        cursor.execute(f'UPDATE users SET {column} = ? WHERE name = ?', (value, name))
        database.commit()
        database.close()
