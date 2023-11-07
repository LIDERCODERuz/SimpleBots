from aiogram.dispatcher.filters.state import StatesGroup,State

class step(StatesGroup):
    start = State()
    search = State()
