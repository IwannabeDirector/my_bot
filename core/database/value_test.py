import sqlite3
import os


def take_value(column):
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute("""
		SELECT CASE 
			WHEN SUM({}) IS NULL THEN 1
			ELSE 0
		END AS result 
		FROM users;
	""".format(column))

	result = cursor.fetchone()[0]
	database.close()

	return result
