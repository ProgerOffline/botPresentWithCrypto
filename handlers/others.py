# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp, _

from database import account_api
from keyboards import reply


@dp.message_handler(content_types="contact", is_sender_contact=True)
async def login_in(message: types.Message):
    user = {
        "id" : message.from_user.id,
        "phone_number" : message.contact.phone_number,
        "username" : message.from_user.username,
        "first_name" : message.from_user.first_name,
        "last_name" : message.from_user.last_name,
    }

    await account_api.create_account(user)
    await message.answer(
        text=_("💻 Добро пожаловать в личный кабинет"),
        reply_markup=reply.main_menu(),
    )