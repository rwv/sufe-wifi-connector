#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from importlib import import_module

from config import login_config, other_config
from utils.test_connection import test_connection

user_os = import_module('utils.{}'.format(other_config['os']))
network_type = import_module('model.{}'.format(login_config['type']))

network_info = user_os.get_wifi_interface()
for i in network_info:
    if not test_connection():
        print('Unable to connect the internet')
        if i['ssid'] == 'sufe-{}'.format(login_config['type']):
            print('Current Network SSID is {}'.format('sufe-{}'.format(login_config['type'])))
            network_type.wifi_portal_login(login_config['username'], login_config['password'])
