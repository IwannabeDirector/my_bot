from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove


def rereg_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Возраст', callback_data='age')],
        [InlineKeyboardButton(text='Дату рождения', callback_data='birthday')]
    ])

    return keyboard


rmk = ReplyKeyboardRemove()