from aiogram import Bot
from aiogram.types import Message
from aiogram import Router, F

from core.database.take_all_users import take_reg_users

# 3
roulette = Router()

@roulette.message(F.text == '/pidor@o4ko_bibka_bot')
async def start_pidor_roulette():
	participants = take_reg_users()
	print(participants)


@roulette.message(F.text == '/run@o4ko_bibika_bot')
async def start_run_roulette():
	pass