# -*- coding: utf-8 -*-

from datetime import datetime
from database.models import Account


async def get_account(user_id: int):
    account = await Account.query.where(
        Account.user_id == user_id
    ).gino.first()

    return account


async def create_account(user: dict):
    old_exist = await get_account(user['id'])

    if not old_exist:
        now = datetime.now()
        auth_date = f"{now.day}.{now.month}.{now.year}"

        account = Account(
            user_id=user['id'],
            username=user['username'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            phone=user['phone_number'],
            ballance=0.0, 
            wallet="⚠️ Добавьте кошелек",
            wallet_pm="⚠️ Добавьте кошелек",
            wallet_crypto="⚠️ Добавьте кошелек",
            auth_date=auth_date,
            sponsor_id=0,
        )
        await account.create()

        return account
    return old_exist


async def update_ballance(user_id: int, new_amount: float):
    account = await get_account(user_id)
    await account.update(
        ballance=new_amount,
    ).apply()

    return account