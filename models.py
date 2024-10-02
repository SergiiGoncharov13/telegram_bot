from pydantic import BaseModel
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Film(BaseModel):
    name:str
    description:str
    rating:float
    genre:str
    actors:list[str]
    poster:str


class FilmForm(StatesGroup):
    name = State()
    description = State()
    raiting = State()
    genge = State()
    actors = State()
    poster = State()

