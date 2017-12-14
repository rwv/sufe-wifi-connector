from utils.log import logging
from utils.perpetualTimer import perpetualTimer
from utils.test_connection import test_connection


class Connector:
    """
    A class of sufe wifi auto-connetor.
    """

    def __init__(self, ssid, wifi, detect_interval):
        """
        Initialize the connector class

        :param ssid: the instance of utils.ssid.SSID class
        :param wifi: the instance of model.Wifi class
        :param detect_interval: the interval of detecting internet connection
        """
        logging.info('sufe-wifi connector init')
        self.__ssid = ssid
        self.__wifi = wifi
        self.__detect_interval = detect_interval
        self.__previous_ssid = ''
        self.__connect_timer = perpetualTimer(0, lambda: None)
        self.__connect_timer.cancel()
        self.status = False

    def start(self):
        """
        Start the auto-connector
        """
        logging.info('sufe-wifi connector start')
        self.__connect()
        self.__connect_timer = perpetualTimer(self.__detect_interval, self.__connect)
        self.__connect_timer.start()
        self.status = True

    def __connect(self):
        """
        detect the internet connection and ssid and login if not connected to internet and ssid is the related ssid
        """
        network_ssid = self.__ssid.get()
        logging.debug('Current Network SSID is {}'.format(network_ssid))
        if self.__ssid.check():
            if self.__previous_ssid != network_ssid:
                logging.info('Current Network SSID is {}'.format(network_ssid))
                self.__previous_ssid = network_ssid
            if not test_connection():
                try:
                    self.__wifi.login()
                except Exception as e:
                    logging.critical('Login Failed: {}'.format(str(e)))
        else:
            self.__wifi.cancel_heartbeat()
            if self.__previous_ssid != network_ssid:
                logging.info('Current Network SSID is {}'.format(network_ssid))
                self.__previous_ssid = network_ssid

    def stop(self):
        """
        Stop the auto-connector
        """
        self.__connect_timer.cancel()
        self.__wifi.logout()
        logging.info('sufe-wifi connector stop')
        self.status = False
