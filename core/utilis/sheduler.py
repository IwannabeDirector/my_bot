import aioschedule
import asyncio
from aiogram import Bot

from core.handlers.roulette import start_run_roulette, start_pidor_roulette
from core.database.delete_from_database import delete_data


async def start_roulette():
	pass


async def delete_task():
	await delete_data()


# async def run_task():
# 	await message.answer('/pidor@o4ko_bibka_bot')
# 	await start_run_roulette()


async def start_scheduler():
	aioschedule.every().day.at("23:59").do(delete_task)
	aioschedule.every().day.at("11:46").do(start_run_roulette)
	while True:
		await aioschedule.run_pending()
		await asyncio.sleep(1)
