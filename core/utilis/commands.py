from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
	commands = [
		BotCommand(
			command='/start',
			description='Здарова Ебать'
		),
		BotCommand(
			command='/reg',
			description='Регистрация'
		),
		BotCommand(
			command='/rereg',
			description='Изменить данные'
		),
		BotCommand(
			command='/myinfo',
			description='Информация о смешарике'
		)
	]

	await bot.set_my_commands(commands, BotCommandScopeDefault())
