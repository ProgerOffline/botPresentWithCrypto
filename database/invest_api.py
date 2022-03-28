# -*- coding: utf-8 -*-

from datetime import datetime

from database import account_api
from .models import InvestRecord


async def create_record(user_id: int, amount: float):
    now = datetime.now()
    date = f"{now.day}.{now.month}.{now.year}"
    account = await account_api.get_account(user_id)

    record = InvestRecord(
        account_id=account.id,
        user_id=user_id,
        amount=amount,
        date=date,
        count_precent=0,
    )

    await record.create()
    return record


async def get_user_records(user_id=None, account_id=None) -> list:
    records = []

    if user_id:
        records = await InvestRecord.query.where(
            InvestRecord.user_id == user_id,
        ).gino.all()

    if account_id:
        records = await InvestRecord.query.where(
            InvestRecord.account_id == account_id,
        ).gino.all()

    return records


async def get_invest_record(invest_id: int):
    record = await InvestRecord.query.where(
        InvestRecord.id == invest_id
    ) .gino.first()

    return record


async def delete_record(invest_id: int):
    record = await get_invest_record(invest_id)
    await record.delete()
