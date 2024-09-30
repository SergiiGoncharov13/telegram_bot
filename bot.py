import asyncio
import logging
import sys
import json

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, URLInputFile


from command import FILM_COMMAND, START_COMMAND, FILMS_BOT_COMMAND, START_BOT_COMMAND
from data import get_films
from keybords import film_keyboard_markup, FilmCallback
from models import Film




TOKEN = 'Token'
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}')




@dp.message(FILM_COMMAND)
async def films(message:Message):
    data = get_films()
    markup = film_keyboard_markup(film_list=data)
    await message.answer(f'List of films', reply_markup = markup)

@dp.callback_query(FilmCallback.filter())
async def callb_film(callback: CallbackQuery, callback_data: FilmCallback):
    film_id = callback_data.id
    film_data = get_films(film_id=film_id)
    film = Film(**film_data)
    text = (
        f"Фільм: {film.name}\n"
        f"Опис: {film.description}\n"
        f"Рейтинг: {film.rating}\n"
        f"Жанр: {film.genre}\n"
        f"Актори: {', '.join(film.actors)}\n"
    )
   
    await callback.message.answer_photo(
        caption=text, photo=URLInputFile(
            film.poster,
            filename=f'{film.name}_poster.{film.poster.split('.')[-1]}'
            )
        )


async def main():
    bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        ),
    )
    await dp.start_polling(bot)
    # await bot.set_my_commands(
    #     [
    #         FILMS_BOT_COMMAND,
    #         START_BOT_COMMAND
    #     ]
    # )




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())




