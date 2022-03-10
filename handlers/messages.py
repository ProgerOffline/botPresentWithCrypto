# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp

from database import account_api
from keyboards import reply


# Пользователь отправил свой контакт
@dp.message_handler(content_types="contact", is_sender_contact=True)
async def login_in(message: types.Message):
    contact = types.Contact()
    contact.user_id = message.from_user.id
    contact.phone_number = int(message.contact.phone_number)
    contact.first_name = message.from_user.username

    await account_api.create_account(contact)
    await message.answer(
        text="💻 Добро пожаловать в личный кабинет",
        reply_markup=reply.main_menu(),
    )