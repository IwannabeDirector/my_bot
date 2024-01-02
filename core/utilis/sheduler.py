import asyncio

from aiogram import Bot

from core.handlers.scheduler_roulette import scheduler_pidor_roulette, scheduler_run_roulette
from core.database.delete_from_database import delete_data
from core.database.scheduler_roulette_test import scheduler_roulette_test


async def start_roulette(bot: Bot):
	if scheduler_roulette_test('pidor_day') == 1:
		await scheduler_pidor_roulette(bot)
	else:
		pass

	await asyncio.sleep(3)

	if scheduler_roulette_test('run_day') == 1:
		await scheduler_run_roulette(bot)
	else:
		pass


async def delete_task():
	await delete_data()
