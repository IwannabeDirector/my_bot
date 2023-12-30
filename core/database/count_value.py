import sqlite3
import os


def count_value(name, column):
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	if name and column:
		cursor.execute(f"UPDATE users SET {column} = COALESCE({column}, 0) + 1 WHERE name = ?", (name,))
		database.commit()
		database.close()
