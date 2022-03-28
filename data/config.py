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

MAX_REFERAL_LEVELS = 10
REFERAL_PRECENT_LEVELS = {
    0 : 6,
    1 : 3,
    2 : 3,
    3 : 1,
    4 : 0.5,
    5 : 0.5,
    6 : 0.5,
    7 : 0.2,
    8 : 0.2,
    9 : 0.1,
}

FOREX_WEBSITE = "https://foxverse.me"
FOREX_TELEGRAM_COMMUNITY = "https://t.me/foxversemetaverse"
FOREX_TELEGRAM_CHANNEL = "https://t.me/foxverseme"
FOREX_TWITTER = "https://twitter.com/foxverseme"
FOREX_MEDIUM = "https://medium.com/@foxverse.me"
FOREX_YOUTUBE = "https://www.youtube.com/channel/UCsdWJEX0HoAD6Gh9Kqco4tQ"

FOREX_LICENSE = "https://foxverse.me/license"
FOREX_POLICY = "https://foxverse.me/privacy"
FOREX_TERM = "https://foxverse.me/privacy"

FOREX_WHITEPAPER_ENG = "https://google.com"
FOREX_WHITEPAPER_CNINESE = "https://google.com"

FOREX_BANNER_120X120 = "https://google.com"
FOREX_BANNER_120X600 = "https://google.com"
FOREX_BANNER_160X600 = "https://google.com"
FOREX_BANNER_300X600 = "https://google.com"
FOREX_BANNER_468X60 = "https://google.com"
FOREX_BANNER_720X300 = "https://google.com"
FOREX_BANNER_728X90 = "https://google.com"

FOREX_CHAINSKE = "http://www.chainske.com/a/show.php?itemid=47506"
FOREX_5BITE =  "http://www.5bite.com/post/10365.html"
FOREX_BLOCKCHAIN_ECONOMY = "http://www.blockchaineconomy.com.cn/be/2022/03/21/29852.html"
FOREX_CAJINGKU = "https://caijingku.net/hongguan/20220321246040.html"
FOREX_MY_TOKEN = "https://www.mytokencap.com/news/383183.html"
FOREX_TMT_FORUM = "https://www.tmtforum.com/observe/8117.html"