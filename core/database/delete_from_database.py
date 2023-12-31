import sqlite3
import os


async def delete_data():
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute('UPDATE users SET cocksize_day = NULL WHERE cocksize_day IS NOT NULL')
	cursor.execute('UPDATE users SET pidor_day = NULL WHERE pidor_day IS NOT NULL')
	cursor.execute('UPDATE users SET run_day = NULL WHERE run_day IS NOT NULL')

	database.commit()
	database.close()
