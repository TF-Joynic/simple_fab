#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Administrator'

from utils.DateTime import DateTime


def log(string, *args):
    if not string or not isinstance(string, str):
        return

    print '[' + DateTime.date() + ']' + string.format(*args)
