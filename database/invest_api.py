# -*- coding: utf-8 -*-

from database.models import db, InvestRecords
from datetime import datetime


async def create_record(user_id: int, amount: float):
    now = datetime.now()
    date = f"{now.day}.{now.month}.{now.year}"
    
    record = InvestRecords(
        user_id=user_id,
        amount=amount,
        date=date,
        count_precent=0,
    )

    await record.create()
    return record


async def get_user_records(user_id: int):
    records = await InvestRecords.query.where(
        InvestRecords.user_id == user_id,
    ).gino.all()

    return records


async def get_invest_record(invest_id: int):
    record = await InvestRecords.query.where(
        InvestRecords.id == invest_id
    ) .gino.first()

    return record


async def delete_record(invest_id: int):
    record = await get_invest_record(invest_id)
    await record.delete()
