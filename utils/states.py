from aiogram.fsm.state import State, StatesGroup


class DialogGPTState(StatesGroup):
    """Класс для хранения информации во время диалога"""

    role = State()
    request = State()    
    history = State()


class ChanheAsseccState(StatesGroup):
    """Класс для хранения информации о пользователе"""

    name = State()
    user_id = State()


class ChanheAsseccState_v2(StatesGroup):
    """Класс для хранения информации о пользователе"""

    name = State()
     