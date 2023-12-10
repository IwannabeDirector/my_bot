from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
	await bot.send_message(
		message.from_user.id, f'<b>Добро пожаловать на сервер шизофрения, {message.from_user.first_name}</b>'
	)
