import random
import asyncio

from aiogram import Bot
from aiogram.types import Message
from aiogram import Router, F

from core.database.take_all_users import take_reg_users
from core.database.write_in_database import database_entry
from core.database.value_test import take_value
from core.database.take_day_value import take_day_value
from core.database.count_value import count_value

# 3
roulette = Router()


@roulette.message(F.text == '/pidor@o4ko_bibka_bot')
async def start_pidor_roulette(message: Message, bot: Bot):
	column = 'pidor_day'
	value = 1
	column_count = 'pidor_count'

	if take_value(column):
		participants = take_reg_users('run_day')
		if participants:
			pidor = random.choice(participants)[0]
			await asyncio.sleep(1)
			await message.answer('Кто пидор?')
			await asyncio.sleep(1)
			await message.answer(f'{pidor} - пидор!')
			database_entry(pidor, column, value)
			new_value = count_value(pidor, column_count)

	else:
		pidor = take_day_value(column)
		await message.answer(f'Пидор дня - {pidor}')


@roulette.message(F.text == '/run@o4ko_bibka_bot')
async def start_run_roulette(message: Message, bot: Bot):
	column = 'run_day'
	value = 1
	column_count = 'run_count'

	if take_value(column):
		participants = take_reg_users('pidor_day')
		if participants:
			run = random.choice(participants)[0]
			await asyncio.sleep(1)
			await message.answer('Кто красавчик?')
			await asyncio.sleep(1)
			await message.answer(f'{run} - красавчик!')
			database_entry(run, column, value)
			new_value = count_value(run, column_count)
	else:
		run = take_day_value(column)
		await message.answer(f'Красавчик дня - {run}')
