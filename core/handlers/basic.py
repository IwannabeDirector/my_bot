from aiogram import Bot, Router
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
	await bot.send_message(
		message.chat.id, f'<b>Добро пожаловать на сервер шизофрения, {message.from_user.first_name}</b>'
	)
