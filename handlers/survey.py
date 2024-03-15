from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from pprint import pprint


class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    favourite_genre = State()
    group = State()
    song = State()


survey_router = Router()

@survey_router.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer("Как вас зовут?")

@survey_router.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.set_state(Survey.age)
    await message.answer("Сколько лет?")

@survey_router.message(Survey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text
    if gender == "Мужчина".title or gender == "Пацан".title or gender == "Мужик".title:
        await message.answer("Настоящий мужчина!")
    elif gender == "Женщина".title or gender == "Девушка".title:
        await message.answer("Барыня барыня, сударыня барыня!")
    else:
        await message.answer("Нет такого пола!")
        return
    await state.set_state(Survey.age)
    await message.answer("Сколько лет?")

@survey_router.message(Survey.age)
async def process_genre(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Цифрами")
        return
    elif int(age) > 150:
        await message.answer("Столько люди не живут!")
        return
    elif int(age) >= 90:
        await message.answer("Врёшь? ^_^")
    elif int(age) <= 16:
        await message.answer("Мал, да удал")
    await state.update_data(age=int(age))
    await state.set_state(Survey.favourite_genre)
    await message.answer("Любимый жанр")

@survey_router.message(Survey.favourite_genre)
async def process_favorite(message: types.Message, state: FSMContext):
    favorite = message.text
    await state.set_state(Survey.group)
    await message.answer("Любимая группа/Любимый исполнитель")

@survey_router.message(Survey.group)
async def process_favorite(message: types.Message, state: FSMContext):
    group = message.text
    await state.set_state(Survey.song)
    await message.answer("Любимая песня")

@survey_router.message(Survey.song)
async def procrss_song(message: types.Message, state: FSMContext):
    song = message.text

    data = await state.get_data()
    pprint(data)
    await state.clear
    #await message.answer(f'information')
    