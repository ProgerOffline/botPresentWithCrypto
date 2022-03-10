# -*- coding: utf-8 -*-

from aiogram import executor
from loader import dp
from database import create_db


async def on_startup(dp):
    import middlewares, handlers
    await create_db()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)