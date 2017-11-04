#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from importlib import import_module
from time import sleep

from config import login_config, other_config
from utils.perpetualTimer import perpetualTimer
from utils.test_connection import test_connection

user_os = import_module('utils.{}'.format(other_config['os']))
network_type = import_module('model.{}'.format(login_config['type']))
network_info = user_os.get_wifi_interface()
previous_ssid = ''
wifi = network_info[0]
# Initializing a empty Timer
heartbeat_timer = perpetualTimer(0, lambda: 0)
heartbeat_timer.cancel()
while True:
    if wifi['ssid'] == 'sufe-{}'.format(login_config['type']):
        if previous_ssid != wifi['ssid']:
            print('Current Network SSID is {}'.format(wifi['ssid']))
            previous_ssid = wifi['ssid']
        if not test_connection():
            heartbeat_timer.cancel()
            print('Unable to connect the internet')
            do_heartbeat = network_type.wifi_portal_login(login_config['username'], login_config['password'])
            heartbeat_timer = perpetualTimer(600, do_heartbeat)
            heartbeat_timer.start()
    else:
        heartbeat_timer.cancel()
        if previous_ssid != wifi['ssid']:
            print('Current Network SSID is {}'.format(wifi['ssid']))
            previous_ssid = wifi['ssid']
    sleep(other_config['interval'])
