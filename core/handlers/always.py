from aiogram import Bot
from aiogram.types import Message
from aiogram import F, Router

da = Router()


@da.message((F.text == 'да') | (F.text == 'Да') | (F.text == 'ДА'))
async def get_start(message: Message):
	await message.answer('Хуй на')
