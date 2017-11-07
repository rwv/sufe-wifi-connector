#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from importlib import import_module
from time import sleep

from config import login_config, other_config
from utils.perpetualTimer import perpetualTimer
from utils.test_connection import test_connection

user_os = import_module('utils.{}'.format(other_config['os']))
network_type = import_module('model.{}'.format(login_config['type']))
previous_ssid = ''
# Initializing a empty Timer
heartbeat_timer = perpetualTimer(0, lambda: 0)
heartbeat_timer.cancel()
while True:
    network_ssid = user_os.get_wifi_ssid()
    if network_ssid == 'sufe-{}'.format(login_config['type']):
        if previous_ssid != network_ssid:
            print('Current Network SSID is {}'.format(network_ssid))
            previous_ssid = network_ssid
        if not test_connection():
            heartbeat_timer.cancel()
            print('Fail to connect to the internet')
            print('Trying to login the Wi-Fi portal')
            do_heartbeat = None
            for i in range(other_config['retry-interval']):
                try:
                    do_heartbeat = network_type.wifi_portal_login(login_config['username'], login_config['password'])
                except:
                    print('Portal login failed for {} times'.format(i))
                    pass
                else:
                    print('Login succeeded')
                    break
            if not do_heartbeat:
                raise Exception('Fail to login')
            heartbeat_timer = perpetualTimer(600, do_heartbeat)
            heartbeat_timer.start()
    else:
        heartbeat_timer.cancel()
        if previous_ssid != network_ssid:
            print('Current Network SSID is {}'.format(network_ssid))
            previous_ssid = network_ssid
    sleep(other_config['interval'])
