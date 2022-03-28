# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import REFERAL_PRECENT_LEVELS
from keyboards import ctypes, reply, inline
from loader import dp, _
from database import invest_api, referer_api, account_api
from statesgroup import OutInvest


@dp.callback_query_handler(ctypes.out_invest.filter())
async def show_out_invest(call: types.CallbackQuery, callback_data: dict, 
    state: FSMContext):

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

    await call.answer()


@dp.callback_query_handler(ctypes.referers_levels.filter())
async def get_refer_level(call: types.CallbackQuery, callback_data: dict):
    level = int(callback_data['level'])
    
    # call.message.from_user.id = определяет id бота 🤷‍♂️
    # Пришлось использовать call.message.chat.id
    account = await account_api.get_account(user_id=call.message.chat.id)
    referers = await referer_api.get_referers_at_level(
        account_id=account.id,
        level=level,
    )

    active_referers = await referer_api.get_referers_at_level(
        account_id=account.id,
        level=level,
        only_active=True,
    )

    amount_referers_investition = await referer_api.get_amount_investition(
        referers=active_referers,
    )

    income_referers = 0
    for referer in active_referers:
        investitions = await invest_api.get_user_records(account_id=referer.id)

        for investition in investitions:
            amount = investition.amount
            income_referers += amount / 100 * REFERAL_PRECENT_LEVELS[level-1]
    
    await call.message.edit_text(
        text=f"📈 Линия {level}\n" +\
            f"Рефералов: {len(referers)}\n" +\
            f"Активных рефералов: {len(active_referers)}\n" +\
            f"Всего оборот: {amount_referers_investition} USD\n" +\
            f"Доход: {income_referers} USD",
        reply_markup=inline.back_to_ref_levels(),
    )

    await call.answer()


@dp.callback_query_handler(ctypes.back_to_ref_levels.filter())
async def back_to_ref_levels(call: types.CallbackQuery):
    # call.message.from_user.id = определяет id бота 🤷‍♂️
    # Пришлось использовать call.message.chat.id
    account = await account_api.get_account(call.message.chat.id)
    account_referers = await referer_api.get_all_referers(
        account_id=account.id,
    )

    account_active_referers = await referer_api.get_all_referers(
        account_id=account.id,
        only_active=True,
    )

    amount_referers_investition = await referer_api.get_amount_investition(
        referers=account_active_referers,
    )

    await call.message.answer(
        text=_(
            f"📈 Ваша структура\n" + \
            f"Рефералов: {len(account_referers)}\n" +\
            f"Активных рефералов: {len(account_active_referers)}\n" +\
            f"Всего оборот: {amount_referers_investition} USD\n" +\
            f"Доход: {account.referer_income} USD\n" 
        ),
        reply_markup=inline.referers_levels(),
    )

    await call.answer()


@dp.callback_query_handler(ctypes.foxverse_menu.filter(section="menu"))
async def show_foxverse(call: types.CallbackQuery):
    await call.message.edit_text(
        text="FOXVERSE is a next generation metaverse platform" +\
             "by Hong Kong based Neowiz Play Studio Hong Kong Limited.",
        reply_markup=inline.foxverse_menu()
    )

    await call.answer()


@dp.callback_query_handler(ctypes.foxverse_menu.filter(section="social_media"))
async def forex_website(call: types.CallbackQuery):
    await call.message.edit_text(
        text="🗃 Выберите раздел",
        reply_markup=inline.forexverse_social_media(),
    )

    await call.answer()


@dp.callback_query_handler(ctypes.foxverse_menu.filter(section="whitepaper"))
async def forex_website(call: types.CallbackQuery):
    await call.message.edit_text(
        text="🗃 Выберите раздел",
        reply_markup=inline.foxverse_whitepaper(),
    )

    await call.answer()


@dp.callback_query_handler(ctypes.foxverse_menu.filter(section="banners"))
async def forex_website(call: types.CallbackQuery):
    await call.message.edit_text(
        text="🗃 Выберите раздел",
        reply_markup=inline.foxverse_banners(),
    )

    await call.answer()


@dp.callback_query_handler(ctypes.foxverse_menu.filter(section="media_partners"))
async def forex_website(call: types.CallbackQuery):
    await call.message.edit_text(
        text="🗃 Выберите раздел",
        reply_markup=inline.foxverse_media_partners(),
    )

    await call.answer()