from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from core.settings import settings
from core.handlers.basic import get_start
from core.database import user_info, delete_from_database
from core.handlers import always, cocksize, roulette
from core.utilis import commands, sheduler



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
	scheduler = AsyncIOScheduler(timezone='Asia/Novosibirsk')
	scheduler.add_job(sheduler.start_scheduler, trigger='date', run_date=datetime.now())
	scheduler.start()
	await bot.delete_webhook(drop_pending_updates=True)
	await commands.set_default_commands(bot)
	dp.startup.register(start_bot)
	dp.shutdown.register(stop_bot)
	dp.message.register(get_start, Command(commands=['start']))
	dp.include_router(user_info.router_main)
	dp.include_router(always.da)
	dp.include_router(cocksize.cock_size)
	#dp.include_router(roulette.roulette)
	# await sheduler.start_scheduler()
	try:
		await dp.start_polling(bot)
	finally:
		await bot.session.close()


if __name__ == '__main__':
	asyncio.run(start())
