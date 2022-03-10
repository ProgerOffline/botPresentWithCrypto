# -*- coding: utf-8 -*-

from loader import dp
from data.config import I18N_DOMAIN, LOCALES_DIR
from .logger_midldleware import UpdateLoggerMiddleware
from .language_middleware import ACLMiddleware


def setup_lang_middleware():
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)

    return i18n


if __name__ == "middlewares":
    dp.middleware.setup(UpdateLoggerMiddleware())