import sqlite3
import aioschedule
import time
import os
import asyncio


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

	print('kek')


async def job():
	await delete_data()


async def start_scheduler():
	print('start def first')
	aioschedule.every().day.at("00:00").do(job)
	while True:
		await aioschedule.run_pending()
		await asyncio.sleep(1)
		print('start def')
