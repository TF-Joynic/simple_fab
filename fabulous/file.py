#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/7
"""
import platform

from fabric.operations import local, run

from fabulous.utils.string import render

__author__ = "xiaolei"

import os
from fabric.context_managers import settings
from exception.FileNotFoundError import FileNotFoundError
from fabric.operations import abort
from fabric.colors import red


def check_md5_match(local_file, remote_file):
    if not os.path.exists(local_file):
        raise FileNotFoundError

    with settings(warn_only=True):
        platform_info = str(platform.platform()).lower()

        local_file_md5 = ''
        if 'darwin' in platform_info:
            local_file_md5 = local(render("md5 {}", local_file), capture=True).split(' = ')[1]

        remote_file_md5 = run(render("md5sum {}", remote_file)).split(' ')[0]

        return local_file_md5 == remote_file_md5


def change_mod(abs_file):
    run(render("chmod 0755 {}", abs_file))
    return True


def remove_local_file(abs_file_path):
    if not abs_file_path or not os.path.exists(abs_file_path):
        abort(red(render("file: {} not exists!", abs_file_path)))

    local(render("rm -f {}", abs_file_path))