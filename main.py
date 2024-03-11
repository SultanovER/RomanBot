import asyncio
from bot import bot, dp
import logging
from handlers.start import start_router
from handlers.picture import picture_router


async def main():
    dp.include_routers(start_router, picture_router)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())