# -*- coding: utf-8 -*-

from aiogram import types
from . import ctypes

from data import config 

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


def referers_levels():
    keyboard = types.InlineKeyboardMarkup()

    for i in range(1, 11):
        keyboard.add(
            types.InlineKeyboardButton(
                text=f"Линия {i}",
                callback_data=ctypes.referers_levels.new(
                    level=i,
                ),
            ),
        )
    
    return keyboard


def back_to_ref_levels():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Назад",
            callback_data=ctypes.back_to_ref_levels.new(),
        )
    )


def foxverse_menu():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            text="Website",
            url=config.FOREX_WEBSITE,
        ),
        types.InlineKeyboardButton(
            text="Social Media",
            callback_data=ctypes.foxverse_menu.new(section="social_media"),
        ),
    ).row(
        types.InlineKeyboardButton(
            text="License",
            url=config.FOREX_LICENSE,
        ),
        types.InlineKeyboardButton(
            text="Whitepaper",
            callback_data=ctypes.foxverse_menu.new(section="whitepaper"),
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Banners",
            callback_data=ctypes.foxverse_menu.new(section="banners"),
        ),
        types.InlineKeyboardButton(
            text="Media Partners",
            callback_data=ctypes.foxverse_menu.new(section="media_partners"),
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Privacy Policy",
            url=config.FOREX_POLICY,
        ),
        types.InlineKeyboardButton(
            text="Terms and Conditions",
            url=config.FOREX_TERM,
        ),
    )


def forexverse_social_media():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            text="Telegram Community",
            url=config.FOREX_TELEGRAM_COMMUNITY,
        ),
        types.InlineKeyboardButton(
            text="Telegram Channel",
            url=config.FOREX_TELEGRAM_CHANNEL,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Twitter",
            url=config.FOREX_TWITTER,
        ),
        types.InlineKeyboardButton(
            text="Medium",
            url=config.FOREX_MEDIUM,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Youtube",
            url=config.FOREX_YOUTUBE,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Назад",
            callback_data=ctypes.foxverse_menu.new("menu"),
        ),
    )


def foxverse_whitepaper():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            text="Eng",
            url=config.FOREX_WHITEPAPER_ENG,
        ),
        types.InlineKeyboardButton(
            text="Chinese",
            url=config.FOREX_WHITEPAPER_CNINESE,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Назад",
            callback_data=ctypes.foxverse_menu.new("menu"),
        ),
    )


def foxverse_banners():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            text="120x120",
            url=config.FOREX_BANNER_120X120,
        ),
        types.InlineKeyboardButton(
            text="120x600",
            url=config.FOREX_BANNER_120X600,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="160x600",
            url=config.FOREX_BANNER_160X600,
        ),
        types.InlineKeyboardButton(
            text="300x600",
            url=config.FOREX_BANNER_300X600,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="468x60",
            url=config.FOREX_BANNER_468X60,
        ),
        types.InlineKeyboardButton(
            text="720x300",
            url=config.FOREX_BANNER_720X300,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="728x90",
            url=config.FOREX_BANNER_728X90,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Назад",
            callback_data=ctypes.foxverse_menu.new("menu"),
        ),
    )


def foxverse_media_partners():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            text="Chainske",
            url=config.FOREX_CHAINSKE,
        ),
        types.InlineKeyboardButton(
            text="5Bite",
            url=config.FOREX_5BITE,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Blockchain Economy",
            url=config.FOREX_BLOCKCHAIN_ECONOMY,
        ),
        types.InlineKeyboardButton(
            text="Cajingku",
            url=config.FOREX_CAJINGKU,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="MyToken",
            url=config.FOREX_MY_TOKEN,
        ),
        types.InlineKeyboardButton(
            text="TMT forum",
            url=config.FOREX_TMT_FORUM,
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Назад",
            callback_data=ctypes.foxverse_menu.new("menu"),
        ),
    )