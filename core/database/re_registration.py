from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram import Router, F

import sqlite3
import os
import datetime

from core.utilis.rereg_keyboard import rereg_keyboard, rmk

# [1]
router2 = Router()


class ReRegistrationStates(StatesGroup):
    waiting_for_new_age = State()
    waiting_for_new_birthday = State()


@router2.message(F.text == '/rereg@o4ko_bibka_bot')
async def start_rereg(message: Message, state: FSMContext):
    user_id = message.from_user.id

    base_path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_path, 'reg_base.sqlite')
    database = sqlite3.connect(db_path)
    cursor = database.cursor()

    cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        await message.answer('Сначала зарегайся, чушпан')
    else:
        await message.answer(text='Что ты хочешь изменить', reply_markup=rereg_keyboard())


@router2.callback_query(lambda c: c.data == 'age')
async def update_age(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    await call.message.answer('Введи новый возраст', reply_markup=rmk)
    await state.set_state(ReRegistrationStates.waiting_for_new_age)


@router2.message(ReRegistrationStates.waiting_for_new_age)
async def process_new_age(message: Message, state: FSMContext):
    age = message.text
    if not age.isdigit() or int(age) <= 0 or int(age) > 150:
        await message.answer('Ты чепушила, нормальный возраст введи')
    else:
        await state.update_data(input_age=age)

    if not age.isdigit() or int(age) <= 0 or int(age) > 150:
        await message.answer('Ты чепушила, нормальный возраст введи')
    else:
        user_id = message.from_user.id

        base_path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_path, 'reg_base.sqlite')
        database = sqlite3.connect(db_path)
        cursor = database.cursor()

        cursor.execute(
            'UPDATE users SET age=? WHERE id=?', (age, user_id)
        )
        database.commit()
        database.close()
        await message.answer('Возраст обновлен')
        await state.clear()


@router2.callback_query(lambda c: c.data == 'birthday')
async def update_age(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    await call.message.answer('Введи новую дату рождения', reply_markup=rmk)
    await state.set_state(ReRegistrationStates.waiting_for_new_birthday)


@router2.message(ReRegistrationStates.waiting_for_new_birthday)
async def process_new_age(message: Message, state: FSMContext):
    birthday = message.text
    try:
        datetime.datetime.strptime(birthday, '%Y-%m-%d')
        user_id = message.from_user.id

        base_path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_path, 'reg_base.sqlite')
        database = sqlite3.connect(db_path)
        cursor = database.cursor()

        cursor.execute(
            'UPDATE users SET birthday=? WHERE id=?', (birthday, user_id)
        )
        database.commit()
        database.close()
        await message.answer('Дата обновлена')
        await state.clear()
    except ValueError:
        await message.answer('Ты че , сказано же ГГГГ-ММ-ДД')
