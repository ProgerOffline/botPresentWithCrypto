# -*- coding: utf-8 -*-

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")