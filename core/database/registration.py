from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram import Router, F

import sqlite3
import os
import datetime


# [1]
router1 = Router()


class RegistrationStates(StatesGroup):
	waiting_for_age = State()
	waiting_for_birthday = State()
	waiting_for_update = State()
	waiting_for_new_age = State()
	waiting_for_new_birthday = State()


@router1.message(F.text == '/reg@o4ko_bibka_bot')
async def start_reg(message: Message, state: FSMContext):
	user_id = message.from_user.id

	base_path = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_path, 'reg_base.sqlite')
	database = sqlite3.connect(db_path)
	cursor = database.cursor()

	cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
	existing_user = cursor.fetchone()

	if existing_user:
		await message.answer('Ты уже смешарик')
	else:
		await message.answer(text='Привет пидрила, сколько тебе лет?')
		await state.set_state(RegistrationStates.waiting_for_age)

	database.close()


@router1.message(RegistrationStates.waiting_for_age)
async def process_age(message: Message, state: FSMContext):
	age = message.text
	if not age.isdigit() or int(age) <= 0 or int(age) > 150:
		await message.answer('Ты чепушила, нормальный возраст введи')
	else:
		await state.update_data(input_age=age)
		await message.answer(
			'А родился когда? (формат ГГГГ-ММ-ДД)'
		)
		await state.set_state(RegistrationStates.waiting_for_birthday)


@router1.message(RegistrationStates.waiting_for_birthday)
async def process_birthday(message: Message, state: FSMContext):
	birthday = message.text
	try:
		datetime.datetime.strptime(birthday, '%Y-%m-%d')
		user_data = await state.get_data()
		age = user_data.get('input_age')
		user_id = message.from_user.id
		user_name = message.from_user.first_name
		base_path = os.path.dirname(os.path.abspath(__file__))
		db_path = os.path.join(base_path, 'reg_base.sqlite')
		database = sqlite3.connect(db_path)
		cursor = database.cursor()

		cursor.execute(
			'INSERT INTO users (id, name, age, birthday) VALUES (?, ?, ?, ?)', (user_id, user_name, age, birthday)
		)
		database.commit()
		database.close()
		await message.answer('Чухан, ты зареган')
		print('aa')
		await state.clear()

	except ValueError:
		await message.answer('Чушпан, сказано же ГГГГ-ММ-ДД')
