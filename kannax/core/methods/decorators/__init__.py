# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['Decorators']

from .raw_decorator import RawDecorator  # noqa
from .add_task import AddTask
from .on_cmd import OnCmd
from .on_filters import OnFilters
from .on_left_member import OnLeftMember
from .on_new_member import OnNewMember


class Decorators(AddTask, OnCmd, OnFilters, OnLeftMember, OnNewMember):
    """ methods.decorators """
