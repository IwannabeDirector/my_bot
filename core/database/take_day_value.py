import sqlite3
import os


def take_day_value(column):
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute("""
		SELECT name 
		FROM users
		WHERE {} IS NOT NULL;
	""".format(column))
	result = cursor.fetchone()[0]

	database.close()

	return result
