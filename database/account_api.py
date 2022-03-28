# -*- coding: utf-8 -*-

from datetime import datetime
from .models import Account
from . import referer_api
from loader import bot


async def get_account(user_id=None, account_id=None) -> Account:
    account = None

    if user_id:
        account = await Account.query.where(
            Account.user_id == user_id
        ).gino.first()
    
    if account_id:
        account = await Account.query.where(
            Account.id == account_id
        ).gino.first()

    return account


async def create_account(account: dict) -> Account:
    old_exist = await get_account(account['id'])

    if not old_exist:
        now = datetime.now()
        auth_date = f"{now.day}.{now.month}.{now.year}"

        account = Account(
            user_id=account['id'],
            username=account['username'],
            first_name=account['first_name'],
            last_name=account['last_name'],
            phone=account['phone_number'],
            ballance=0.0, 
            wallet="⚠️ Добавьте кошелек",
            wallet_pm="⚠️ Добавьте кошелек",
            wallet_crypto="⚠️ Добавьте кошелек",
            auth_date=auth_date,
            referer_id=account['referer_id'],
            referer_income = 0,
        )
        await account.create()

        return account
    return old_exist


async def update_ballance(user_id, new_amount):
    account = await get_account(user_id=user_id)
    await account.update(
        ballance=new_amount,
    ).apply()

    return account


async def update_referer_income(account_id, new_amount, precent):
    account = await get_account(account_id=account_id)
    new_amount = account.referer_income + (new_amount / 100 * precent)

    await account.update(
        referer_income=new_amount,
    ).apply()
    await update_ballance(account.user_id, new_amount)

    referer = await referer_api.get_account_referer(
        account_id=account.id,
    )

    await bot.send_message(
        chat_id=account.user_id,
        text="ℹ️ На ваш баланс зачислено реферальное" +\
            f"вознаграждение в размере {new_amount / 100 * precent} USD",
    )

    return referer.referer_id