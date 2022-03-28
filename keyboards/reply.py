# -*- coding: utf-8 -*-

from aiogram import types
from loader import _


def authorization(if_exist):
    if if_exist:
        return types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=1,
        ).add(
            types.KeyboardButton(
                text=_("Войти"),
                request_contact=True,
            ),
        )
    else:
        return types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=1,
        ).add(
            types.KeyboardButton(
                text=_("Регистрация"),
                request_contact=True,
            ),
        )


def main_menu():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
    ).row(
        types.KeyboardButton(text=_("Foxverse")),
        types.KeyboardButton(text=_("Профиль")),
    ).row(
        types.KeyboardButton(text=_("Мой Баланс")),
        types.KeyboardButton(text=_("Пополнить баланс")),
    ).row(
        types.KeyboardButton(text=_("Реферальная программа")),
        types.KeyboardButton(text=_("Кошелек для вывода")),
    ).row(
        types.KeyboardButton(text=_("Мои инвестиции")),
        types.KeyboardButton(text=_("Инвестиционный продукт")),
    ).row(
        types.KeyboardButton(text=_("Вывод средств")),
        types.KeyboardButton(text=_("Вывод тела депозита")),
    ).row(
        types.KeyboardButton(text=_("NFT")),
        types.KeyboardButton(text=_("Поддержка")),
    ).row(
        types.KeyboardButton(text=_("Выход")),
    )


def back_to_menu():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
    ).add(
        types.KeyboardButton(
            text=_("Назад"),
        )
    )


def buy_invest():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
    ).row(
        types.KeyboardButton(
            text=_("Купить"),
        ),
        types.KeyboardButton(
            text=_("Назад"),
        )
    )


def confirm_buy():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
    ).add(
        types.KeyboardButton(
            text=_("Подтвердить"),
        ),
        types.KeyboardButton(
            text=_("Назад"),
        )
    )


def referal_program():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
    ).add(
        types.KeyboardButton(
            text=_("Моя структура"),
        ),
        types.KeyboardButton(
            text=_("Назад"),
        )
    )


def nft_menu():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
    ).row(
        types.KeyboardButton(
            text=_("NFT Self-Minting"),
        ),
        types.KeyboardButton(
            text=_("NFT Market"),
        ),
    ).add(
        types.KeyboardButton(
            text=_("Назад"),
        ),
    )