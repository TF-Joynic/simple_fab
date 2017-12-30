#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/7
"""
import os
from fabric.operations import run, sudo
from fabric.utils import abort
from fabulous.utils.string import render
from exception.InvalidArgumentError import InvalidArgumentError

__author__ = "xiaolei"

NOHUP = "nohup"


def execute_command(command, output=None, nohup=False, append_to_output=True):
    if not command or not isinstance(command, str):
        raise InvalidArgumentError

    cmd = ""
    if nohup:
        cmd = NOHUP + " "

    cmd += command + ((" >> " if append_to_output else " > ") + output + " 2>&1 &") if output else ""
    return run(cmd, pty=False)


def extract_command_pid(command, *args):
    if not command or not isinstance(command, str):
        return None

    greps = ""
    for arg in args:
        greps += " | grep " + arg

    return run(render("ps aux | grep {}{} ", command, greps) + "| awk '{print $2}'")


def install_as_service(remote_jar_path, jar_file_name):
    """
    install as a system service
    """
    if not remote_jar_path or not jar_file_name:
        return False

    symbol = "/etc/init.d/" + jar_file_name.replace(".jar", "")

    if run(render("ls {}", symbol)):
        return True

    create_symbol_link(remote_jar_path, symbol)
    return True


def create_symbol_link(source, target, soft=True):
    sudo(render("ln {}{} {}", ("-s " if soft else ""), source, target))
