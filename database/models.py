# -*- coding: utf-8 -*-

from gino import Gino
from sqlalchemy import sql
from sqlalchemy import (Column, String, Sequence, Integer)


db = Gino()


class Account(db.Model):
    __tablename__ = "accounts"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(Integer)
    username = Column(String)
    user_phone = Column(String)

