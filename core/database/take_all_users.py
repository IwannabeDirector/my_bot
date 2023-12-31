import sqlite3
import os


def take_reg_users(exception):
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()
	if exception:
		cursor.execute(f'SELECT name FROM users WHERE {exception} IS NULL')
	else:
		cursor.execute('SELECT name FROM users')

	names = cursor.fetchall()
	database.close()

	return names
