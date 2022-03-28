# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, _
from database import account_api, referer_api
from keyboards import reply
from statesgroup import Authorization


@dp.message_handler(
    content_types="contact", 
    is_sender_contact=True,
    state=Authorization.get_contact,
)
async def authorization(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        referer_id = data["referer_id"]

    account = {
        "id" : message.from_user.id,
        "phone_number" : message.contact.phone_number,
        "username" : message.from_user.username,
        "first_name" : message.from_user.first_name,
        "last_name" : message.from_user.last_name,
        "referer_id" : referer_id,
    }   

    account = await account_api.create_account(account)
    await referer_api.create_referer_record(
        referer_id=referer_id,
        account_id=account.id
    )
    await message.answer(
        text=_("💻 Добро пожаловать в личный кабинет"),
        reply_markup=reply.main_menu(),
    )
    await state.finish()