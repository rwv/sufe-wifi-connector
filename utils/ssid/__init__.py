class SSID:
    def __init__(self, os, network_type):
        if os == 'windows':
            from .windows import get_wifi_ssid
        elif os == 'mac':
            from .mac import get_wifi_ssid
        else:
            from .linux import get_wifi_ssid
        self.__get = get_wifi_ssid
        self.__network_type = network_type

    def get(self):
        return self.__get()

    def check(self):
        return self.__get() == 'sufe-{}'.format(self.__network_type)
