from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
	commands = [
		BotCommand(
			command='start',
			description='Начало работы'
		),
		BotCommand(
			command='run',
			description='🌈'
		),
		BotCommand(
			command='cancel',
			description='Отмена'
		)
	]

	await bot.set_my_commands(commands, BotCommandScopeDefault())
