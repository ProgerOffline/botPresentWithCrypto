# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.reply import confirm_buy


class BuyInvest(StatesGroup):
    get_amount = State()
    confirm_buy = State()


class ToUpBallance(StatesGroup):
    get_amount = State()


class OutInvest(StatesGroup):
    confirm_out = State()