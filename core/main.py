from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram.client.session.aiohttp import AiohttpSession
import asyncio
import logging

from core.settings import settings
from core.handlers.basic import get_start


async def start_bot(bot: Bot):
	await bot.send_message(settings.bots.admin_id, text='Bot started')


async def stop_bot(bot: Bot):
	await bot.send_message(settings.bots.admin_id, text='Bot stopped')


async def start():
	session = AiohttpSession(proxy='http://proxy.server:3128')
	logging.basicConfig(level=logging.INFO,
						format='%(asctime)s - [%(levelname)s] - %(name)s - '
								'(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
						)
	bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

	dp = Dispatcher()
	dp.startup.register(start_bot)
	dp.shutdown.register(stop_bot)
	dp.message.register(get_start, Command(commands=['start', 'run']))
	try:
		await dp.start_polling(bot)
	finally:
		await bot.session.close()


if __name__ == '__main__':
	asyncio.run(start())
