from aiogram.types import Message
from aiogram import Router, F

import sqlite3
import os

from core.database.registration import router1
from core.database.re_registration import router2


# [1]
router_main = Router()
router_main.include_routers(router1, router2)


@router_main.message(F.text == '/myinfo')
async def user_info(message: Message):
	user_id = message.from_user.id

	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute(
		'SELECT * FROM users WHERE id=?', (user_id,)
	)
	info = cursor.fetchone()
	database.close()
	if info is not None:
		labels = {
			'name': 'Имя',
			'age': 'Возраст',
			'birthday': 'Дата рождения',
			'pidor': 'Пидор дня',
			'run': 'Красавчик дня',
			'artpub': 'Алкаш дня'
		}
		columns = [desc[0] for desc in cursor.description]
		user_info = '\n'.join([f'{labels[column]}: {value}' for column, value in zip(columns, info) if column != 'id'])
		await message.answer(f'{user_info}')
	else:
		await message.answer('Пусто')
