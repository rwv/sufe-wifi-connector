"""
the module of ssid get/check
"""


class SSID:
    """
    the class to get wifi ssid
    """

    def __init__(self, os, network_type):
        """
        Initialize the ssid class

        :param os: the user's operating system type
        :param network_type: the user's isp type
        """
        if os == 'windows':
            from .windows import get_wifi_ssid
        elif os == 'mac':
            from .mac import get_wifi_ssid
        else:
            from .linux import get_wifi_ssid
        self.__get = get_wifi_ssid
        self.__network_type = network_type

    def get(self):
        """
        get the user's ssid

        :return: the ssid of user's system
        """
        return self.__get()

    def check(self):
        """
        check if the ssid is same as ssid related to user's isp

        :return: boolean
        """
        return self.__get() == 'sufe-{}'.format(self.__network_type)
