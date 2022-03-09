# -*- coding: utf-8 -*-

from loader import dp
from .update_logger import UpdateLoggerMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(UpdateLoggerMiddleware())