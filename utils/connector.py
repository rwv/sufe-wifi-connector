from config import login_config, other_config
from utils.test_connection import test_connection
from utils.perpetualTimer import perpetualTimer
from utils.ssid import SSID
from utils.log import logging
from model import Wifi


class Connector:
    def __init__(self):
        logging.info('sufe-wifi connector init')
        logging.debug('login_config: {}'.format(str(login_config)))
        logging.debug('other_config: {}'.format(str(other_config)))
        self.__ssid = SSID(other_config['os'])
        self.__wifi = Wifi(login_config['username'], login_config['password'], login_config['network_type'],
                           other_config['retry_times'],
                           other_config['retry_interval'])
        self.__previous_ssid = ''
        self.__connect_timer = perpetualTimer(0, lambda: None)
        self.__connect_timer.cancel()
        self.status = False

    def start(self):
        logging.info('sufe-wifi connector start')
        self.__connect_timer = perpetualTimer(other_config['detect_interval'], self.__connect)
        self.__connect_timer.start()
        self.status = True

    def __connect(self):
        network_ssid = self.__ssid.get()
        logging.debug(network_ssid)
        if network_ssid == 'sufe-{}'.format(login_config['network_type']):
            if self.__previous_ssid != network_ssid:
                logging.info('Current Network SSID is {}'.format(network_ssid))
                self.__previous_ssid = network_ssid
            if not test_connection():
                self.__wifi.login()
        else:
            self.__wifi.cancel_heartbeat()
            if self.__previous_ssid != network_ssid:
                logging.info('Current Network SSID is {}'.format(network_ssid))
                self.__previous_ssid = network_ssid

    def stop(self):
        self.__connect_timer.cancel()
        self.__wifi.cancel_heartbeat()
        self.__wifi.logout()
        logging.info('sufe-wifi connector stop')
        self.status = False

    def reload(self):
        logging.info('sufe-wifi connector reload')
        logging.debug('login_config: {}'.format(str(login_config)))
        logging.debug('other_config: {}'.format(str(other_config)))
        self.__wifi = Wifi(login_config['username'], login_config['password'], login_config['network_type'],
                           other_config['retry_times'],
                           other_config['retry_interval'])
        if self.status:
            self.stop()
            self.start()
