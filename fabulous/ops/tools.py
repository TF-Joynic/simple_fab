#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/7
"""

__author__ = "xiaolei"

import os
import socket
from fabulous.exception.InvalidArgumentError import InvalidArgumentError


def port_occupied(port, host="127.0.0.1"):
    if not str.isdigit(str(port)):
        raise InvalidArgumentError

    if not host or isinstance(host, str):
        raise InvalidArgumentError

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except:
        return False