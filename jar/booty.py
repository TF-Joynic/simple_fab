#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/6
"""
import time

from fabric.colors import green, red

__author__ = "xiaolei"

import os
import sys

sys.path.insert(0, "..")

from fabric.context_managers import lcd, cd
from fabric.decorators import task, runs_once
from fabric.operations import local, run, sudo
from fabric.utils import abort

from fabulous.utils.string import render

from fabric.state import env
from fabulous.file_transfer import upload_file_to_remote
from fabulous.file import check_md5_match, change_mod
from fabulous.server import execute_command, extract_command_pid, install_as_service
from config import booty

env.project_name = booty.project_name
env.lang = booty.lang

env.hosts = booty.hosts
env.user = booty.user
env.password = booty.password

env.local_dir = booty.local_dir
env.maven_cmd = booty.maven_cmd
env.jar_file_name = booty.jar_file_name
env.local_jar_path = booty.local_jar_path
env.remote_dir = booty.remote_dir
env.server_start_cmd = booty.server_start_cmd
env.server_stop_cmd = booty.server_stop_cmd
env.server_restart_cmd = booty.server_restart_cmd
env.server_status_cmd = booty.server_status_cmd
# env.server_start_and_restart_param = "--spring.profiles.active=" + booty.


@task
def release():
    pack()

    print "pack fin~"

    upload()
    print "upload ok"

    check_file_match()

    restart()

    print "release & restart ok!"


@task
def pack():
    with lcd(env.local_dir):
        local(render(env.maven_cmd))


@task
def upload():
    local_abs_jar_path = os.sep.join([env.local_jar_path, env.jar_file_name])
    if not os.path.exists(local_abs_jar_path):
        abort(render("{} not found", local_abs_jar_path))

    if not env.remote_dir:
        abort("not valid remote_dir")

    upload_file_to_remote(local_abs_jar_path, env.remote_dir)


@task
def check_file_match():
    if not check_md5_match(os.sep.join([env.local_jar_path, env.jar_file_name]),
                           os.sep.join([env.remote_dir, env.jar_file_name])):
        abort("local and remote file not match!")

    print "file md5 matched, proceed"


def check_install_as_service():
    """
    Decorator
    True if is a system service, False otherwise
    :return: boolean
    """
    if not install_as_service(os.sep.join([env.remote_dir, env.jar_file_name]), env.project_name):
        abort("not install as service")


@task
def status():
    run(env.server_status_cmd)


@task
def start():
    """
    start server on remote
    """
    with cd(env.remote_dir):
        change_mod(env.jar_file_name)
        run(env.server_start_cmd, pty=False)

    red("server started")


@task
def stop():
    """
    stop server
    """
    run(env.server_stop_cmd, pty=False)


@task
def restart():
    """
    TODO: smoothly stop
    """
    run(env.server_restart_cmd, pty=False)
