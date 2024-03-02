import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

dispatcher = Dispatcher()

def hello_user(name):
    return f"Привет, {name}!\nДобро пожаловать в ToDoList бот"

@dispatcher.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(hello_user(message.from_user.full_name))


async def main():
    bot = Bot("6780267645:AAFV_zn5GE_8Ihb4sC57pzUHeVVWK0qQer8")
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())