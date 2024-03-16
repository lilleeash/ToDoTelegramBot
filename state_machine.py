from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import  State, StatesGroup

storage = MemoryStorage()

class FSMTaskForm(StatesGroup):
    fill_task = State()
    fill_description = State()
    fill_priority = State()