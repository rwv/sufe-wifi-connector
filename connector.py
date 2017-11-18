#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep

from config import login_config, other_config
from utils.test_connection import test_connection
from utils.ssid import SSID
from utils.log import logging
from model import Wifi

logging.info('sufe-wifi-connector started')
logging.debug('login_config: {}'.format(str(login_config)))
logging.debug('other_config: {}'.format(str(other_config)))

ssid = SSID(other_config['os'])
wifi = Wifi(login_config['username'], login_config['password'], login_config['type'], other_config['retry-times'],
            other_config['retry-interval'])

previous_ssid = ''
while True:
    network_ssid = ssid.get()
    logging.debug(network_ssid)
    if network_ssid == 'sufe-{}'.format(login_config['type']):
        if previous_ssid != network_ssid:
            logging.info('Current Network SSID is {}'.format(network_ssid))
            previous_ssid = network_ssid
        if not test_connection():
            Wifi.login()
    else:
        wifi.cancel_heartbeat()
        if previous_ssid != network_ssid:
            logging.info('Current Network SSID is {}'.format(network_ssid))
            previous_ssid = network_ssid
    sleep(other_config['interval'])
