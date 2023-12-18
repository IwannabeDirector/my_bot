import asyncio
import sqlite3
import schedule
import time
import os


def delete_data():
	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute('UPDATE FROM users WHERE cocksize = Null')

	database.commit()
	database.close()


def job():
	delete_data()


def start_scheduler():
	schedule.every().day.at("00:00").do(job)
	while True:
		schedule.run_pending()
		time.sleep(1)
