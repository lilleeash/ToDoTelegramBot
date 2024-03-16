import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from setup_database import *
from read_task_sql import *
from state_machine import *

dispatcher = Dispatcher()
storage = MemoryStorage()
create_task_button = KeyboardButton(text='Посмотреть задачу')
read_tasks_button = KeyboardButton(text='Создать задачу')
keyboard = ReplyKeyboardMarkup(keyboard=[[create_task_button, read_tasks_button]])

def hello_user(name):
    return f"Привет, {name}!\nДобро пожаловать в ToDoList бот"

@dispatcher.message(F.text == 'Посмотреть задачи')
async def read_tasks(message: Message):
    if read_task_sql():
        await message.answer(f"Ваши задачи:\n{read_task_sql()}")
    else:
        await message.answer("У вас пока нет задач!")

@dispatcher.message(F.text == 'Создать задачу', StateFilter(default_state))
async def create_task(message: Message):
    await message.answer(text='Для создания задачи введите команду /createtask')

@dispatcher.message(Command(commands='createtask'))
async def fill_title(message: Message, state: FSMContext):
    await message.answer(text="Введите название задачи")
    await state.set_state(FSMTaskForm.fill_task)


@dispatcher.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(hello_user(message.from_user.full_name), reply_markup=keyboard)

async def main():
    bot = Bot("6780267645:AAFV_zn5GE_8Ihb4sC57pzUHeVVWK0qQer8")
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    setup_database()
    asyncio.run(main())




# connection = sqlite3.connect("todo.db")
# cursor_obj = connection.cursor()
#
# cursor_obj.execute("""INSERT INTO task(ID, title, description, priority, is_done, user_id)
#     VALUES (1, "Название задачи", "Описание задачи", "Высокий", "TRUE", 1)
# """)
#
# connection.commit()