# -*- coding: utf-8 -*-

import re
from gino import Gino
from sqlalchemy import (Column, String, Sequence, Integer, Float)
from sqlalchemy.sql.sqltypes import BigInteger


db = Gino()


class Account(db.Model):
    __tablename__ = "accounts"
    id = Column(BigInteger, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(BigInteger)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    ballance = Column(Float)
    language = Column(String(2))
    wallet = Column(String)
    wallet_pm = Column(String)
    wallet_crypto = Column(String)
    auth_date = Column(String)
    referer_id = Column(BigInteger)
    referer_income = Column(BigInteger)


class InvestRecord(db.Model):
    __tablename__ = "invest_records"
    id = Column(BigInteger, Sequence("invest_id_seq"), primary_key=True)
    account_id = Column(BigInteger)
    user_id = Column(BigInteger)
    amount = Column(Float)
    date = Column(String)
    count_precent = Column(Integer)


class Referer(db.Model):
    __tablename__ = "referers"
    id = Column(BigInteger, Sequence("referer_id_seq"), primary_key=True)
    referer_id = Column(BigInteger)
    account_id = Column(BigInteger)
