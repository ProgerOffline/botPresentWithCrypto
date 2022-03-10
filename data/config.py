# -*- coding: utf-8 -*-

import os
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
DB_HOST = env.str("DB_HOST")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")

I18N_DOMAIN = "botprecent"
BASE_DIR = os.getcwd()
LOCALES_DIR = f"{BASE_DIR}/locales"