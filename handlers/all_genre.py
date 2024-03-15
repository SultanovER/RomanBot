from aiogram import F, Router, types


genres_router = Router()

@genres_router.callback_query(F.data == "genres")
async def choose_genre(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Пост-панк"), 
             types.KeyboardButton(text="Панк")],
            [types.KeyboardButton(text="Гранж")],
            [types.KeyboardButton(text="Глэм")],
            [types.KeyboardButton(text="Металл")]
        ]
    )
    await callback.message.answer("Выберите жанр", reply_markup=kb)

@genres_router.message(F.text.lower() == "Панк")
async def show_genres(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Различные жанры", reply_markup=kb)
    
