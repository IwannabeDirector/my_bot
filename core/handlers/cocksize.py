import random

from aiogram import Bot
from aiogram.types import Message
from aiogram import Router, F

import random

cocksize = Router()

step_0 = ["🤬", "😤", "😡", "👿", "😠", "🤡"]
step_5 = ["😧", "🥺", "😱", "😯", "😮", "😓"]
step_10 = ["😰", "😩", "😦", "😣", "😥", "🙁"]
step_15 = ["😐", "😬", "😑", "🙄", "🤭"]
step_20 = ["😎", "🤓", "🤠", "🥳", "😋"]
step_25 = ["🤩", "😇", "😘"]

@cocksize.message(F.text == '/cocksize@o4ko_bibka_bot')
async def analysis_cock_size(message: Message, bot: Bot):
	user_id = message.from_user.id
	cocksize = round(random.gauss(12, 20))

	if cocksize <= 1:
		await message.answer(f"My dick is less 1 cm {random.choice(step_0)}")
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAECfHllf8hnH4BKqSeE0P1GjQI1hoGXogAC6BkAAvHpIElMUTQG1lAkfDME')

	if 1 < cocksize <= 5:
		await message.answer(f"My dick is {str(cocksize)} cm {random.choice(step_5)}")
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAECfHdlf8hCzIt9J4G8yV-6Z8yKMbMkqwACMhgAAubVMUrwHJqAPt6cVDME')

	if 5 < cocksize <= 10:
		await message.answer(f"My dick is {str(cocksize)} cm {random.choice(step_10)}")
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAECfGtlf8ZUEC2KZrXIwxRY7PXSjXhc8gAChxcAAgwIIUlw7wJkhh8RGzME')

	if 10 < cocksize <= 15:
		await message.answer(f"My dick is {str(cocksize)} cm {random.choice(step_15)}")
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAECfH1lf8j8T64VzfkumV-K1_JOX0DBAQACJSYAAitfqEirqLZjBytafTME')

	if 15 < cocksize <= 20:
		await message.answer(f"My dick is {str(cocksize)} cm {random.choice(step_20)}")
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAECfH9lf8kKKMHTAAEWMrQoTvdhchbIPiYAAiQbAAISByBJFS9eruUGkeYzBA')

	if 20 < cocksize <= 25:
		await message.answer(f'My dick is {str(cocksize)} cm {random.choice(step_25)}')
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgQAAxkBAAECfINlf8kruHU2TpB-1-5PZkMU8jYKOQADCgACCDfQU62EjbJsCr1ZMwQ')

	if 25 < cocksize <= 30:
		await message.answer(f'My dick is {str(cocksize)} cm {random.choice(step_25)}')
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgQAAxkBAAECfIFlf8ki8Fp-CY7QPIDyDjsuwTHL8AACEAsAAuY3OFNOHV2yQSpyPzME')

	if cocksize > 30:
		await message.answer(f'My dick is {str(cocksize)} cm {random.choice(step_25)}')
		await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAECfHtlf8iJD3OlSyepE2SbRRTWY2_YkgAC9kIAAv3TsEsdWgq-OhKkJzME')
