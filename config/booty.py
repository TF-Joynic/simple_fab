#!/usr/bin/env python
# encoding=utf-8

"""
    project: simple_fab
    date: 2017/9/6
"""

__author__ = "xiaolei"

project_name = "booty"
lang = "java"

hosts = ["192.168.1.100:22"]
user = "###"
password = "####"

local_dir = "/Users/xiaolei/java/booty"
maven_cmd = "mvn -U clean package -DskipTests=true"
jar_file_name = "booty.jar"
local_jar_path = "/Users/xiaolei/java/booty/target"
remote_dir = "/root/xiaolei/booty"
server_start_cmd = "service " + project_name + " start"
server_stop_cmd = "service " + project_name + " stop"
server_restart_cmd = "service " + project_name + " restart"
server_status_cmd = "service " + project_name + " status"
active_profile_dev = "dev"
active_profile_test = "test"
active_profile_production = "production"

