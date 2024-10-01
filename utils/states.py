from aiogram.fsm.state import State, StatesGroup


class DialogGPTState(StatesGroup):
    """Класс для хранения информации во время диалога"""

    role = State()
    request = State()    
    history = State()
    