import aioschedule
import asyncio
from datetime import datetime

from aiogram.types import Message, Chat
from aiogram import Bot

from core.handlers.roulette import start_run_roulette, start_pidor_roulette
from core.database.delete_from_database import delete_data
from core.database.scheduler_roulette_test import scheduler_roulette_test
from core.settings import settings


async def start_roulette():
	if scheduler_roulette_test('pidor_day') == 1:
		pass
	if scheduler_roulette_test('run_day') == 1:
		pass


async def delete_task():
	await delete_data()


async def send_message(bot: Bot, chat_id: int, text: str) -> int:
	message = await bot.send_message(chat_id, text)
	return message.message_id


async def start_scheduler():
	chat_id = -4079228075
	bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
	message_id = await send_message(bot, chat_id, 'Roulette_time')
	message = Message(message_id=message_id, date=datetime.now(), chat=Chat(id=chat_id, type="private"))

	aioschedule.every().day.at("23:59").do(delete_task)
	aioschedule.every().day.at("16:28").do(lambda: asyncio.create_task(start_pidor_roulette(message, bot)))
	await asyncio.sleep(5)
	aioschedule.every().day.at("16:28").do(lambda: asyncio.create_task(start_run_roulette(message, bot)))
	while True:
		await aioschedule.run_pending()
		await asyncio.sleep(10)

