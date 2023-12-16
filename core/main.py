from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio
import logging

from core.settings import settings
from core.handlers.basic import get_start
from core.database import user_info


async def start_bot(bot: Bot):
	await bot.send_message(settings.bots.admin_id, text='Bot started')


async def stop_bot(bot: Bot):
	await bot.send_message(settings.bots.admin_id, text='Bot stopped')


async def start():
	#session = AiohttpSession(proxy='http://proxy.server:3128')
	logging.basicConfig(level=logging.INFO,
						format='%(asctime)s - [%(levelname)s] - %(name)s - '
								'(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
						)
	bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

	dp = Dispatcher()
	await bot.delete_webhook(drop_pending_updates=True)
	dp.startup.register(start_bot)
	dp.shutdown.register(stop_bot)
	dp.message.register(get_start, Command(commands=['start']))
	dp.include_router(user_info.router_main)
	try:
		await dp.start_polling(bot)
	finally:
		await bot.session.close()


if __name__ == '__main__':
	asyncio.run(start())
