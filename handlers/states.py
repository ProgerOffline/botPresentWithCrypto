# -*- coding: utf-8 -*-

from re import L
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, _
from database import account_api, invest_api, referer_api
from statesgroup import BuyInvest, OutInvest, ToUpBallance, NFT
from keyboards import reply


@dp.message_handler(text=_("Назад"), state=NFT.back_to_nft_menu)
async def back_to_nft_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=_("🗃 Выберите раздел"),
        reply_markup=reply.nft_menu(),
    )


@dp.message_handler(text=_("Назад"), state='*')
async def back_to_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=_("🗃 Выберите раздел"),
        reply_markup=reply.main_menu(),
    )


@dp.message_handler(text=_("Подтвердить"), state=OutInvest.confirm_out)
async def confirm_out(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        record_id = data['record_id']
        finished = data['finished']

    record = await invest_api.get_invest_record(record_id)
    account = await account_api.get_account(message.from_user.id)

    if finished:
        amount = record.amount + (record.amount / 100 * record.count_precent)
    else:
        amount = record.amount + (record.amount / 100 * (record.count_precent) - 20)

    await account_api.update_ballance(
        user_id=account.user_id,
        new_amount=account.ballance + amount,
    )

    await invest_api.delete_record(record_id)

    await state.finish()
    await message.answer(
        text=_("✅ Средства поступили на ваш баланс. "),
        reply_markup=reply.main_menu(),
    )


@dp.message_handler(state=BuyInvest.get_amount)
async def get_amount_invest(message: types.Message, state: FSMContext):
    account = await account_api.get_account(message.from_user.id)

    try:
        amount = float(message.text)
    except ValueError:
        await message.answer(
            text=_("Вам стоит ввести число"),
        )
        return
    
    if amount < 100:
        await message.answer(
            text=_("⚠️Ошибка: Минимальная сумма инвестиции 100.00 USD"),
        )
        return
    
    if amount > account.ballance:
        await message.answer(
            text=_("⚠️Ошибка: На балансе недостаточно средств"),
            reply_markup=reply.main_menu(),
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['amount'] = amount
    
    await BuyInvest.confirm_buy.set()
    await message.answer(
        text=_(f"Вы совершаете покупку инвестиционного продукта на сумму {amount} USD"),
        reply_markup=reply.confirm_buy(),
    )

@dp.message_handler(state=BuyInvest.confirm_buy, text=_("Подтвердить"))
async def confirm_buy(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        amount = data['amount']

    account = await account_api.get_account(message.from_user.id)
    await account_api.update_ballance(
        user_id=account.user_id,
        new_amount=account.ballance - amount,
    )
    await invest_api.create_record(
        user_id=message.from_user.id,
        amount=amount
    )

    referer = await referer_api.get_account_referer(account.id)
    if referer.referer_id != 0:
        await referer_api.pay_referers_system(referer.referer_id, amount)

    await message.answer(
        text=_(
            "✅ Инвестиционный продукт успешно оплачен. " +\
            "Каждые 24 часа вы будете получать дивиденды."
        ),
        reply_markup=reply.main_menu(),
    )

    await state.finish()


@dp.message_handler(state=ToUpBallance.get_amount)
async def get_amount_ballance(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text)
    except ValueError:
        await message.answer(
            text=_("Вам стоит ввести число"),
        )
        return
    
    account = await account_api.get_account(message.from_user.id)
    await account_api.update_ballance(
        user_id=account.user_id, 
        new_amount=account.ballance + amount,
    )

    await message.answer(
        text=_("Баланс успешно пополнен."),
        reply_markup=reply.main_menu(),
    )
    await state.finish()