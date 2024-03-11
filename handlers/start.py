from aiogram import Router, types, F
from aiogram.filters import Command
import logging

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Прочисть разум!", url="https://youtu.be/hTWKbfoikeg?si=qZkRUbK7E_mfwve0")
            ],
            [
                types.InlineKeyboardButton(text="О боте", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Егор Летов", callback_data="Letov"),
                types.InlineKeyboardButton(text="Мёртвые", url="https://youtu.be/LzhyASowsSQ?si=AkTCOp7S4z4QAQ4N&t=16")
                
            ],
            [
                types.InlineKeyboardButton(text="Курт Кобейн", callback_data="Cobain"),
                types.InlineKeyboardButton(text="Come as you are", url="https://youtu.be/vabnZ9-ex7o?si=faAMalgqTEwSx-5E")
            ],
            [
                types.InlineKeyboardButton(text="Виктор Цой", callback_data="Tsoy"),
                types.InlineKeyboardButton(text="Спокойная ночь", url="https://youtu.be/HHLZRx3EImQ?si=i4AdwOfQhJPQdX-X")
            ]
        ]
    )
    logging.info(message.from_user)
    await message.answer(f"Привет {message.from_user.username}", reply_markup=kb)

@start_router.callback_query(F.data == "about")
async def cool(callback: types.CallbackQuery):
    await callback.message.answer("Всякая информация про рок-музыкантов и творчестве их и пр.")

@start_router.callback_query(F.data == "Cobain")
async def kurt(callback: types.CallbackQuery):
    await callback.message.answer("Курт Дональд Кобейн - лидер группы NIRVANA, которую основал вместе с Кристом Новоселичем(бас-гитарист). Родился в Абердине 1967")

@start_router.callback_query(F.data == "Letov")
async def egor(callback: types.CallbackQuery):
    await callback.message.answer("Игорь Фёдорович Летов, он же Егор Летов, был рождён в Омске 1964. Был человеком начитанным и эрудированным. Известен своими неординарными песнями. Отец сибирского андеграунда. Был инициатором таких проектов, как; Гражданская Оборона, Посев, Коммунизм и т.д.")

@start_router.callback_query(F.data == "Tsoy")
async def victor(callback: types.CallbackQuery):
    await callback.message.answer("Цой жив!... Виктор Робертович Цой - легенда!... Родился в Ленинграде. 1962 года рождения. Отец - Роберт Максимович Цой кореец, инженер; мать - Валентина Васильевна Гусева русская, учительница физ-культуры...  Увлекался музыкой, живописью, боевыми искусствами!... Тут даже не надо ничего говорить! ")