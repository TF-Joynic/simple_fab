#!/usr/bin/env python
# encoding=utf-8

__author__ = "xiaolei"

"""
    thrift service file generator

    project: simple_fab
    date: 2017/9/13
"""

project_name = "booty"
lang = "java"

hosts = ["192.168.1.100:22"]
user = "###"
password = "####"

remote_gen_dir = "/root/thrift_idl"
remote_gen_command = "thrift --gen java --gen php --gen py"
remote_gen_java_dir = "gen-java"
remote_gen_php_dir = "gen-php"
remote_gen_python_dir = "gen-py"

remote_pack_file_name = "thrift_simple_fab.tar.gz"
remote_pack_command = "tar -zcvf " + remote_pack_file_name + " -R "\
                      + " ".join([remote_gen_java_dir, remote_gen_php_dir, remote_gen_python_dir])




