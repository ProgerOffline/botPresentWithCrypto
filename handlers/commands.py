# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp, _
from database import account_api
from keyboards import reply


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if_exist = await account_api.get_account(message.from_user.id)
    await message.answer(
        text=_("👋 Добро пожаловать в чат бот инвестиционной платформы eCrypto"),
        reply_markup=reply.authorization(if_exist),
    )
