from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo
import asyncio
import logging

from core.settings import settings
from aiogram.filters import Command
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
	await set_commands(bot)
	await bot.send_message(settings.bots.admin_id, text='Bot started')


async def stop_bot(bot: Bot):
	await bot.send_message(settings.bots.admin_id, text='Bot stopped')


async def start():
	logging.basicConfig(level=logging.INFO,
						format='%(asctime)s - [%(levelname)s] - %(name)s - '
								'(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
						)
	bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

	dp = Dispatcher()
	dp.startup.register(start_bot)
	dp.shutdown.register(stop_bot)
	dp.message.register(get_photo, F.photo)
	dp.message.register(get_start, Command(commands=['start', 'run']))
	try:
		await dp.start_polling(bot)
	finally:
		await bot.session.close()


if __name__ == '__main__':
	asyncio.run(start())
