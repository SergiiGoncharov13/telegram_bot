import asyncio
import logging
import sys
import json

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, URLInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup



from command import FILM_CREATE_COMMAND, BOT_COMMAND, FILMS_COMMAND, START_COMMAND
from data import get_films, add_film
from keybords import film_keyboard_markup, FilmCallback
from models import Film, FilmForm




TOKEN = 'BOT_TOKEN'
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}')




@dp.message(FILMS_COMMAND)
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

@dp.message(FILM_CREATE_COMMAND)
async def film_create(message:Message, state:FSMContext) -> None:
    await state.set_state(FilmForm.name)
    await message.answer(f'Enter film name', reply_markup=ReplyKeyboardRemove())

@dp.message(FilmForm.name)
async def film_name(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FilmForm.description)

@dp.message(FilmForm.description)
async def film_description(message: Message, state:FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(FilmForm.raiting)

@dp.message(FilmForm.raiting)
async def film_rating(message: Message, state:FSMContext):
    await state.update_data(rating=message.text)
    await state.set_state(FilmForm.genge)

@dp.message(FilmForm.genge)
async def film_ganre(message: Message, state:FSMContext):
    await state.update_data(ganre=message.text)
    await state.set_state(FilmForm.actors)

@dp.message(FilmForm.actors)
async def film_actors(message: Message, state:FSMContext):
    await state.update_data(actors=message.text)
    await state.set_state(FilmForm.poster)

@dp.message(FilmForm.poster)
async def film_poster(message: Message, state:FSMContext):
    data = await state.update_data(poster=message.text)
    film = Film(**data)
    add_film(film.model_dump())
    await state.clear()








async def main():
    bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        ),
    )
    await bot.set_my_commands(BOT_COMMAND)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())




