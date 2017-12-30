#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/7
"""
from fabric.context_managers import cd, settings
from fabric.contrib.console import confirm
from fabric.operations import run, put, get
from fabric.utils import abort

from fabulous.utils.string import render

__author__ = "xiaolei"

import os


def upload_file_to_remote(abs_file_path, remote_dir):
    if not abs_file_path or not remote_dir:
        abort("invalid args!")

    if not os.path.isfile(abs_file_path):
        abort(render("file {} not found!", abs_file_path))

    run(render("mkdir -m 0755 {}", remote_dir), quiet=True)
    with cd(remote_dir):

        with settings(warn_only=True):
            upload_result = put(abs_file_path, remote_dir)

            if upload_result.failed and not confirm("upload file failed! Continue ? [Y/N]"):
                abort("upload aborted")


def fetch_file_from_remote(abs_file_path, local_dir):
    if not abs_file_path or not os.path.isdir(local_dir):
        abort("invalid args!")

    get(abs_file_path, local_dir)
