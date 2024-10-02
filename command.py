from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand


FILMS_COMMAND = Command("films")
START_COMMAND = Command("start")
FILM_CREATE_COMMAND = Command('create_film')

BOT_COMMAND = [
    BotCommand(command='films', description='See list of films'),
    BotCommand(command='start', description='bot start'),
    BotCommand(command='create_film', description='add new film')
]
