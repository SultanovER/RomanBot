from aiogram import Router, types, F
from aiogram.filters import Command
import logging
from db.base import Database

from keyboards.all_keyboards import start_kb

music_router = Router()

@music_router.callback_query(F.data == "albums")
async def alb(callback: types.CallbackQuery):
    db = Database()
    album = db.select_albums()
    for i in album:
        text = (f"название: {i[1]}\nгод выпуска: {i[3]}")
        await callback.message.answer(text=text)


@music_router.callback_query(F.data == "groups")
async def groups(callback: types.CallbackQuery):
    db = Database()
    group = db.select_groups()
    for i in group:
        text = (f"Группа: {i[1]}\nЖанр: {i[2]}")
        await callback.message.answer(text=text)