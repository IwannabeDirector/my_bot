import aioschedule
import asyncio
from aiogram import Bot

from core.database.delete_from_database import delete_data


async def start_roulette():
	pass


async def delete_task():
	await delete_data()


async def run_task():
	await start_roulette()


async def start_scheduler():
	aioschedule.every().day.at("11:01").do(delete_task)
	aioschedule.every().day.at("12:00").do(start_roulette)
	while True:
		print('1')
		await aioschedule.run_pending()
		await asyncio.sleep(1)
