# -*- coding: utf-8 -*-

from aiogram import types


def authorization(exist):
    """
    Возвращает одну кнопку входа, если пользователь есть в базе
    То текст будет "Войти", если нет в базе тогда "Регистрация"
    agrs:
        in_base - Наличие пользователя в базе
    """
    if exist:     
        return types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=1,
        ).add(
            types.KeyboardButton(
                text="Войти",
                request_contact=True,
            ),
        )
    else:
        return types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=1,
        ).add(
            types.KeyboardButton(
                text="Регистрация",
                request_contact=True,
            ),
        )


def main_menu():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
    ).row(
        types.KeyboardButton(text="Мой Баланс"),
        types.KeyboardButton(text="Пополнить баланс"),
    ).row(
        types.KeyboardButton(text="Реферальная программа"),
        types.KeyboardButton(text="Кошелек для вывода"),
    ).row(
        types.KeyboardButton(text="Мои инвестиции"),
        types.KeyboardButton(text="Инвестиционный продукт"),
    ).row(
        types.KeyboardButton(text="Вывод средств"),
        types.KeyboardButton(text="Вывод тела депозита"),
    ).row(
        types.KeyboardButton(text="Профиль"),
        types.KeyboardButton(text="Поддержка"),
    ).row(
        types.KeyboardButton(text="Выход"),
    )

