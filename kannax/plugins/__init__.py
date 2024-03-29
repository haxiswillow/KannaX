# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ["ROOT", "get_all_plugins"]

import sys
from os.path import dirname
from typing import List

from kannax import logging
from kannax.utils import get_import_path

_LOG = logging.getLogger(__name__)
ROOT = dirname(__file__)


def get_all_plugins() -> List[str]:
    """list all plugins"""
    plugins = get_import_path(
        ROOT, "/dev/" if len(sys.argv) == 2 and sys.argv[1] == "dev" else "/**/"
    )
    _LOG.debug("All Available Plugins: %s", plugins)
    return list(plugins)
