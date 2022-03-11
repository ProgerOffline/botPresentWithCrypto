# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import ctypes, reply
from loader import dp, _
from database import invest_api
from statesgroup import OutInvest


@dp.callback_query_handler(ctypes.out_invest.filter())
async def show_out_invest(
        call: types.CallbackQuery, callback_data: dict, state: FSMContext
    ):

    async with state.proxy() as data:
        data['record_id'] = int(callback_data['id'])

    await OutInvest.confirm_out.set()
    await call.message.edit_text(
        text=_("‼️ Инвестиционный период продукта не окончен." +\
            "Комиссия вывода составит 20%"),
        reply_markup=reply.confirm_buy(),
    )