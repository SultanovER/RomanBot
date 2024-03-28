from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="we are the champions", url="https://youtu.be/04854XqcfCY?si=kb1nDCEtxBqaSK1H")
            ],
            [
                InlineKeyboardButton(text="Список жанров", callback_data="genres")
            ],
            [
                InlineKeyboardButton(text="Группы", callback_data="groups")
            ],
            [
                InlineKeyboardButton(text="Альбомы", callback_data="albums")
            ]
        ]
    )
    return kb