# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, _
from database import account_api
from statesgroup import Authorization
from keyboards import reply


@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    args = message.get_args()
    async with state.proxy() as data:
        if "referer" in args:
            data['referer_id'] = int(args.split("_")[1])
        
        else:
            data['referer_id'] = 0

    if_exist = await account_api.get_account(message.from_user.id)
    await Authorization.get_contact.set()
    await message.answer(
        text=_("👋 Добро пожаловать в чат бот инвестиционной платформы eCrypto"),
        reply_markup=reply.authorization(if_exist),
    )
