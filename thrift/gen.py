#!/usr/bin/env python
# encoding=utf-8

__author__ = "xiaolei"

"""
    project: simple_fab
    date: 2017/9/26
"""

import sys

sys.path.append("../")

import os
from fabric.api import *

from config import thrift
from fabric.state import env
from fabulous.utils.string import render
from fabulous.file_transfer import upload_file_to_remote, fetch_file_from_remote
from fabric.colors import blue, red, green
from fabulous.file import remove_local_file

env.hosts = thrift.hosts
env.user = thrift.user
env.password = thrift.password

env.remote_gen_dir = thrift.remote_gen_dir
env.remote_gen_command = thrift.remote_gen_command
env.remote_gen_java_dir = thrift.remote_gen_java_dir
env.remote_gen_php_dir = thrift.remote_gen_php_dir
env.remote_gen_python_dir = thrift.remote_gen_python_dir

env.remote_pack_file_name = thrift.remote_pack_file_name
env.remote_pack_command = thrift.remote_pack_command


@task
def gen(idl_path):
    if not idl_path or not os.path.exists(idl_path):
        abort("idl not found")

    idl_path_dir = os.path.dirname(idl_path)
    idl_file_name = os.path.basename(idl_path)
    print(red(render("gen files under dir: {}", idl_path_dir)))

    upload_idl_file(idl_path)

    clear_gen_files()

    gen_thrift_file(idl_file_name)
    pack()
    download(idl_path_dir)
    unpack(idl_path_dir)
    delete_pack_file(idl_path_dir)


@task
def upload_idl_file(abs_file_path):
    if not abs_file_path or not os.path.exists(abs_file_path):
        abort(render("thrift idl file: {} not found!"))

    upload_file_to_remote(abs_file_path, env.remote_gen_dir)


def clear_gen_files():

    clear_dirs = (env.remote_gen_java_dir, env.remote_gen_python_dir, env.remote_gen_php_dir)
    for clear_dir in clear_dirs:
        with cd(os.sep.join([env.remote_gen_dir, clear_dir])):
            run(render("rm -fr *"))

        print(red(render("delete all under: {} ok", clear_dir)))


@task
def gen_thrift_file(thrift_idl_file_name):
    with cd(env.remote_gen_dir):
        run(render("{} {}", env.remote_gen_command, thrift_idl_file_name))

    print(blue(render("gen ok under: {}", env.remote_gen_dir)))


def pack():
    with cd(env.remote_gen_dir):
        run(env.remote_pack_command)

    print(green("pack file fin~"))


def download(local_dir):
    with cd(env.remote_gen_dir):
        fetch_file_from_remote(env.remote_pack_file_name, local_dir)


def unpack(local_dir):
    with lcd(local_dir):
        local(render("tar -zvxf {}", env.remote_pack_file_name))

    print(blue("unpack ok"))


def delete_pack_file(local_dir):
    remove_local_file(os.sep.join([local_dir, env.remote_pack_file_name]))
