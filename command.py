from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand


START_COMMAND = Command('start')
FILM_COMMAND = Command('films')
FILMS_BOT_COMMAND = BotCommand(command='films', description='See list of films')
START_BOT_COMMAND = BotCommand(command='start', description='bot start')