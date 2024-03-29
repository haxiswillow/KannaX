# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['get_collection']

import asyncio
from typing import List

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection

from kannax import logging, Config, logbot

_LOG = logging.getLogger(__name__)
_LOG_STR = "$$$>>> %s <<<$$$"

logbot.edit_last_msg("Connecting to Database ...", _LOG.info, _LOG_STR)

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(Config.DB_URI)
_RUN = asyncio.get_event_loop().run_until_complete

if "KannaX" in _RUN(_MGCLIENT.list_database_names()):
    _LOG.info(_LOG_STR, "KannaX Database Found :) => Now Logging to it...")
else:
    _LOG.info(_LOG_STR, "KannaX Database Not Found :( => Creating New Database...")

_DATABASE: AgnosticDatabase = _MGCLIENT["KannaX"]
_COL_LIST: List[str] = _RUN(_DATABASE.list_collection_names())


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    if name in _COL_LIST:
        _LOG.debug(_LOG_STR, f"{name} Collection Found :) => Now Logging to it...")
    else:
        _LOG.debug(_LOG_STR, f"{name} Collection Not Found :( => Creating New Collection...")
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()


logbot.del_last_msg()
