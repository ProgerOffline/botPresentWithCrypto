# -*- coding: utf-8 -*-

from database import invest_api, account_api
from .models import Referer
from data.config import MAX_REFERAL_LEVELS, REFERAL_PRECENT_LEVELS


async def get_account_referer(account_id: int) -> Referer:
    referer = await Referer.query.where(
        Referer.account_id == account_id,
    ).gino.first()

    return referer


async def get_referer_record(referer_id: int):
    record = await Referer.query.where(
        Referer.id == referer_id,
    ).gino.first()

    return record


async def create_referer_record(referer_id: int, account_id) -> Referer:
    old_exist = await get_account_referer(account_id)

    if not old_exist:
        referer_record = Referer(
            referer_id=referer_id,
            account_id=account_id
        )

        await referer_record.create()
        return referer_record

    return old_exist


async def get_account_referers(account_id: int) -> list:
    referers = await Referer.query.where(
            Referer.referer_id == account_id,
        ).gino.all()
    
    return referers


async def get_all_referers(account_id: int, current_level: int=0,
    last_level: int=MAX_REFERAL_LEVELS, only_active=False) -> list:

    if current_level >= MAX_REFERAL_LEVELS or \
        current_level >= last_level:
        return []

    referers = await get_account_referers(account_id)

    result = []
    for referer in referers:

        if only_active:
            invest_records = await invest_api.get_user_records(
                account_id=referer.account_id,
            )

            if len(invest_records) > 0:
                result.append(referer)

        else:
            result.append(referer)

        sub_referers = await get_all_referers(
            account_id=referer.id,
            current_level=current_level+1,
            last_level=last_level,
            only_active=only_active,
        )

        if sub_referers:
            result += sub_referers

    return result


async def get_referers_at_level(account_id: int, level: int, only_active=False):
    referers_current_level = await get_all_referers(
        account_id=account_id,
        last_level=level,
        only_active=only_active,
    )

    referers_previous_level = await get_all_referers(
        account_id=account_id,
        last_level=level-1,
        only_active=only_active,
    )

    referers_current_level = [r.id for r in referers_current_level]
    referers_previous_level = [r.id for r in referers_previous_level]
    result = list(set(referers_current_level) - set(referers_previous_level))

    result = [
        await get_referer_record(id_)
        for id_ in result
    ]

    return result


async def get_amount_investition(referers):
    amount = 0

    for referer in referers:
        records = await invest_api.get_user_records(
            account_id=referer.account_id
        )
        
        for record in records:
            count_precent = 1 \
                if record.count_precent == 0 \
                else record.count_precent

            amount += record.amount * count_precent
    
    return amount


async def pay_referers_system(account_id, amount):
    for i in range(MAX_REFERAL_LEVELS):
        if account_id == 0:
            return

        account_id = await account_api.update_referer_income(
            account_id=account_id,
            new_amount=amount,
            precent=REFERAL_PRECENT_LEVELS[i],
        )