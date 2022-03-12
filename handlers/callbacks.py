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

    record = await invest_api.get_invest_record(int(callback_data['id']))
    async with state.proxy() as data:
        data['record_id'] = int(callback_data['id'])
        data['finished'] = True
        text = "‼️ Инвестиционный период продукта окончен. Комиссия вывода составит 0%"

        if record.count_precent < 200:
            data['finished'] = False
            text = _("‼️ Инвестиционный период продукта не окончен." +\
                "Комиссия вывода составит 20%")

    await OutInvest.confirm_out.set()
    await call.message.delete()
    await call.message.answer(
        text=text,
        reply_markup=reply.confirm_buy(),
    )