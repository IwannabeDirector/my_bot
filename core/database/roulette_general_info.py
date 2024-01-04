from aiogram.types import Message
from aiogram import Router, F

import sqlite3
import os


# [4]
roulette_info = Router()


@roulette_info.message(F.text == '/pidorstats@o4ko_bibka_bot')
async def user_info(message: Message):
	user_id = message.from_user.id

	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute(
		'SELECT name, pidor_count FROM users WHERE pidor_count IS NOT NULL'
	)
	rows = cursor.fetchall()
	database.close()

	sorted_rows = sorted(rows, key=lambda tup: tup[1], reverse=True)
	results = "\n".join([f'{i + 1}) {row[0]} - {row[1]} раз(а)' for i, row in enumerate(sorted_rows)])
	await message.answer(f'Результаты 🌈ПИДОР Дня\n{results}')


@roulette_info.message(F.text == '/runstats@o4ko_bibka_bot')
async def user_info(message: Message):
	user_id = message.from_user.id

	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute(
		'SELECT name, run_count FROM users WHERE run_count IS NOT NULL'
	)
	rows = cursor.fetchall()
	database.close()

	sorted_rows = sorted(rows, key=lambda tup: tup[1], reverse=True)
	results = "\n".join([f'{i + 1}) {row[0]} - {row[1]} раз(а)' for i, row in enumerate(sorted_rows)])
	await message.answer(f'🎉 Результаты Красавчик Дня\n{results}')
