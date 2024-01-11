import sqlite3
import os


def cock_value(user_id):
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute("""
		SELECT CASE 
			WHEN cocksize_day IS NULL THEN 1
			ELSE 0
		END AS result 
		FROM users
		WHERE id = ?;
	""", (user_id,))

	result = cursor.fetchone()[0]
	database.close()

	return result


def cock_in_db(user_id, column, value):
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	if user_id and column and value:
		cursor.execute(f'UPDATE users SET {column} = ? WHERE id = ?', (value, user_id))
		database.commit()
		database.close()


def return_day_value(user_id):
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute("""
		SELECT cocksize_day
		FROM users
		WHERE id = ?;
	""", (user_id,))
	result = cursor.fetchone()

	database.close()

	return result


