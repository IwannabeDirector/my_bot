from aiogram import Bot
from aiogram.types import Message
from aiogram import Router, F

import random

from core.utilis.cocksize_meme_base import main
from core.database.cocksize_db import *

cock_size = Router()


async def send_response(message, bot, penis_size: float, emoji: str, sticker: str):
	if penis_size <= 1:
		await message.answer(f"My dick is less 1 cm {emoji}")
	else:
		await message.answer(f"My dick is {penis_size} cm {emoji}")
	await bot.send_sticker(chat_id=message.chat.id, sticker=sticker)


@cock_size.message(F.text == '/cocksize@o4ko_bibka_bot')
async def analysis_cock_size(message: Message, bot: Bot):
	user_id = message.from_user.id
	if cock_value(user_id) == 1:
		cock_size = round(random.gauss(12, 10))

		group_boundaries = {1: 0, 5: 1, 10: 2, 15: 3, 20: 4, 25: 5, 30: 6, float('inf'): 7}

		def get_group(cock_size):
			if cock_size <= 0:
				return 0
			for boundary, group in sorted(group_boundaries.items(), reverse=False):
				if cock_size <= boundary:
					return group

		grp = get_group(cock_size)
		emoji, sticker = main(grp)

		await send_response(message, bot, cock_size, emoji, sticker)

		cock_in_db(user_id, "cocksize_day", cock_size)

	else:
		size = return_day_value(user_id)[0]
		if size <= 1:
			await message.answer(f"Your dick is less 1 cm")
		else:
			await message.answer(f"Your dick is {size} cm")
