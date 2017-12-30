#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/7
"""

__author__ = "xiaolei"

import os


def dr(func):
    print "vod"
    return func


@dr
def dr_vd():
    print "king"


dr_vd()
