from aiogram import Router, types
from aiogram.filters import Command
import os
import random

picture_router = Router()

folder = "images"

@picture_router.message(Command("pic"))
async def send_pic(message: types.Message):
    photo_file = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random_photo_file = os.path.join(folder, random.choice(photo_file))
    file = types.FSInputFile(random_photo_file)
    await message.answer_photo(file)