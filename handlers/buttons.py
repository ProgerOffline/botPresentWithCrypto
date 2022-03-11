from sqlalchemy import util


# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, _

from keyboards import reply, inline
from database import account_api, invest_api
from statesgroup import BuyInvest, ToUpBallance


@dp.message_handler(text=_("Мой Баланс"))
async def show_ballance(message: types.Message):
    account = await account_api.get_account(message.from_user.id)

    await message.answer(
        text=_(f"Текущий баланс: {account.ballance} USD"),
    )


@dp.message_handler(text=_("Профиль"))
async def show_account(message: types.Message):
    account = await account_api.get_account(message.from_user.id)
    account.sponsor_id = "Нет спонсора" \
        if account.sponsor_id == 0 \
        else account.sponsor_id

    await message.answer(
        text=_(
            f"Имя: {account.first_name}\n" +\
            f"Фамилия: {account.last_name}\n" +\
            f"ID: {account.id}\n" +\
            f"ID Спонсора: {account.sponsor_id} \n" +\
            f"Кошелек: {account.wallet}\n" +\
            f"Кошелек PM: {account.wallet_pm}\n" +\
            f"Кошелек BTC: {account.wallet_crypto}\n" +\
            f"Дата регистрации: {account.auth_date}\n"
        ),
        reply_markup=reply.back_to_menu(),
    )


@dp.message_handler(text=_("Инвестиционный продукт"))
async def invest_product(message: types.Message):
    await message.answer(
        text=_(
            "ЕЖЕДНЕВНЫЙ ДОХОД:\n" + \
            "   🔸Апрель - 2% в день\n" + \
            "   🔸Май - 3% в день\n" + \
            "   🔸Июнь - 4% в день\n" + \
            "   🔸Июль - 5% в день\n" + \
            "   🔸Август - 6% в день\n\n" + \
            "▪️Стоимость: от 100.00 USD\n" + \
            "▪️Покупка: BTC / ETH / LTC / BCH / USDT TRC20 / TRX / BNB / Perfect Money\n" + \
            "▪️Вывод дивидендов:  USDT TRC20 и Perfect Money (мин. сумма 10.00 USD)\n" + \
            "▪️Время работы инвестиции: до 200% профита (ROI 300%)\n" + \
            "▪️Вывод тела депозита: в любое время с комиссией 20%. Или без комиссии при достижении 200% прибыли.\n"
        ),
        reply_markup=reply.buy_invest(),
    )


@dp.message_handler(text=_("Купить"))
async def buy_invest(message: types.Message):
    await BuyInvest.get_amount.set()
    await message.answer(
        text=_("💵 Введите сумму инвестиции в USD"),
        reply_markup=reply.back_to_menu(),
    )


@dp.message_handler(text=_("Поддержка"))
async def support(message: types.Message):
    await message.answer(
        text=_("👩‍💻 По всем вопросам обращайтесь в нашу техподдержку @crptxprt"),
        reply_markup=reply.back_to_menu(),
    )


@dp.message_handler(text=_("Выход"))
async def logout(message: types.Message):
    if_exist = await account_api.get_account(message.from_user.id)
    
    await message.answer(
        text=_("🙏🏻 Спасибо, что вы с нами! Мы ждем вас снова"),
        reply_markup=reply.authorization(if_exist),
    )


@dp.message_handler(text=_("Пополнить баланс"))
async def to_up_ballance(message: types.Message):
    await ToUpBallance.get_amount.set()
    await message.answer(
        text=_("💵 Введите сумму в USD"),
        reply_markup=reply.back_to_menu(),
    )


@dp.message_handler(text=_("Мои инвестиции"))
async def show_invest_list(message: types.Message):
    records = await invest_api.get_user_records(message.from_user.id)
    
    if len(records) <= 0:
        await message.answer(
            text=_("💵 Инвестиций не найдено"),
        )
        return

    content = [
        _(
            f"💵 Инвестиционный продукт: {record.amount} USD " +\
            f"от {record.date}. Всего начислено {record.count_precent}"+\
            f"/ {record.amount}$"
        )
        for record in records
    ]

    await message.answer(
        text="\n".join(content),
    )


@dp.message_handler(text=_("Вывод тела депозита"))
async def out_body_invest(message: types.Message):
    records = await invest_api.get_user_records(message.from_user.id)

    await message.answer(
        text=_("Выберите тело депозита инвестиционного продукта для вывода:"),
        reply_markup=inline.out_invest_records(records),
    )