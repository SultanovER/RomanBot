import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv, listdir, path 
import os
import random
import logging

folder = 'images'


load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Привет {message.from_user.username}")


@dp.message(Command("pic"))
async def send_rpic(message: types.Message):
    photo_file = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random_photo_file = os.path.join(folder, random.choice(photo_file))
    file = types.FSInputFile(random_photo_file)
    await message.answer_photo(file)

@dp.message(Command("myinfo"))
async def send_myinfo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f'Ваш id: {message.from_user.id}\nВаше имя: {message.from_user.username}')



@dp.message()
async def echo(message: types.Message):
    await message.answer("Привет!")
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())