from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class FilmCallback(CallbackData, prefix='film', sep=';'):
    id : int
    name : str


def film_keyboard_markup(film_list, offset:int|None=None, skip:int|None=None):
    builder = InlineKeyboardBuilder()
    builder.adjust(1, repeat=True)
    for index, film_data in enumerate(film_list):
        callback_data = FilmCallback(id=index, **film_data)
        builder.button(
            text=f'{callback_data.name}',
            callback_data=callback_data.pack()
        )
    builder.adjust(1, repeat=True)
    return builder.as_markup()

