import asyncio
from bot import bot, dp, db
from aiogram import Bot
import logging
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.all_genre import genres_router
from handlers.survey import survey_router


async def on_startup(bot: Bot):
    db.drop_tables()
    db.create_tables()
    db.populate_tables()

async def main():
    dp.include_routers(start_router, picture_router, genres_router, survey_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())