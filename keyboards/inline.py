# -*- coding: utf-8 -*-

from aiogram import types
from . import ctypes


def out_invest_records(records: list):
    keybaord = types.InlineKeyboardMarkup()
    
    for record in records:
        keybaord.add(
            types.InlineKeyboardButton(
                text=f"{record.amount} $",
                callback_data=ctypes.out_invest.new(
                    id=record.id,
                )
            )
        )

    return keybaord