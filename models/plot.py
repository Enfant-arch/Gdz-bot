from aiogram.dispatcher.filters.state import State, StatesGroup

class Search_GDZ(StatesGroup):
    subject = State()
    class_ = State()
    author =  State()
    prgh = State()
    number = State()
class Sendsss(StatesGroup):
    message = State()
