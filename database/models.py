# -*- coding: utf-8 -*-

from gino import Gino
from sqlalchemy import sql
from sqlalchemy import (Column, String, Sequence, Integer, Float, Boolean)
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
    sponsor_id = Column(BigInteger)


class InvestRecords(db.Model):
    __tablename__ = "invest_records"
    id = Column(BigInteger, Sequence("invest_id_seq"), primary_key=True)
    user_id = Column(BigInteger)
    amount = Column(Float)
    date = Column(String)
    count_precent = Column(Integer)