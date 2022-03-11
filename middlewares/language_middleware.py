# -*- coding: utf-8 -*-

from typing import Any, Tuple

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from database.account_api import get_account


async def get_lang(user_id: int):
    account = await get_account(user_id)

    if account:
        return account.language


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user = types.User.get_current()

        return await get_lang(user.id) or user.locale