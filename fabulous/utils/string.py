#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/7
"""

__author__ = "xiaolei"


def render(string, *args):
    if not string or not isinstance(string, str):
        return

    return string.format(*args)