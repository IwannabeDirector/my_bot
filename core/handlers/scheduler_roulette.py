import random
import asyncio

from aiogram import Bot

from core.database.take_all_users import take_reg_users
from core.database.write_in_database import database_entry
from core.database.value_test import take_value
from core.database.take_day_value import take_day_value
from core.database.count_value import count_value


chat_id = -4079228075


async def scheduler_pidor_roulette(bot: Bot):
    column = 'pidor_day'
    value = 1
    column_count = 'pidor_count'

    if take_value(column):
        participants = take_reg_users('run_day')
        if participants:
            pidor = random.choice(participants)[0]
            await asyncio.sleep(1)
            await bot.send_message(chat_id=chat_id, text=f'Кто пидор?')
            await asyncio.sleep(1)
            await bot.send_message(chat_id=chat_id, text=f'{pidor} - пидор!')
            database_entry(pidor, column, value)
            new_value = count_value(pidor, column_count)

    else:
        pidor = take_day_value(column)
        await bot.send_message(chat_id=chat_id, text=f'Пидор дня - {pidor}')


async def scheduler_run_roulette(bot: Bot):
    column = 'run_day'
    value = 1
    column_count = 'run_count'

    if take_value(column):
        participants = take_reg_users('pidor_day')
        if participants:
            run = random.choice(participants)[0]
            await asyncio.sleep(1)
            await bot.send_message(chat_id=chat_id, text=f'Кто красавчик?')
            await asyncio.sleep(1)
            await bot.send_message(chat_id=chat_id, text=f'{run} - красавчик!')
            database_entry(run, column, value)
            new_value = count_value(run, column_count)

    else:
        run = take_day_value(column)
        await bot.send_message(chat_id=chat_id, text=f'Красавчик дня - {run}')