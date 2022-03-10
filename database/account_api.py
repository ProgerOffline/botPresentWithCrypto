# -*- coding: utf-8 -*-

from database.models import Account


async def exist(user_id: int):
    exist = await Account.query.where(
        Account.user_id == user_id
    ).gino.first()

    return exist


async def create_account(contact):
    print(contact)
