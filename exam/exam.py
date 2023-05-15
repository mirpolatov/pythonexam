import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
import os


logging.basicConfig(level=logging.INFO)

bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_menu(message: Message):
    await message.answer('HEllo')


@dp.message_handler()
async def group(msg: Message):
    v = msg.text
    vol = 'AOUIEaioue'
    c = 0
    for i in v:
        if i in vol:
            c += 1
    if c >= 5:
        await msg.delete()
        await msg.answer('o''chirildi')
    else:
        await msg.answer('UNLI harflar 5tadan kam')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)