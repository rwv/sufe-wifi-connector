class SSID:
    def __init__(self, os):
        if os == 'windows':
            from .windows import get_wifi_ssid
        elif os == 'mac':
            from .mac import get_wifi_ssid
        else:
            from .linux import get_wifi_ssid
        self.__get = get_wifi_ssid

    def get(self):
        return self.__get()
