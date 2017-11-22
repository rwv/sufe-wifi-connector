from utils.perpetualTimer import perpetualTimer
from utils.log import logging
from time import sleep


class Wifi:
    def __init__(self, username, password, net_type, retry_times=10, retry_interval=5):
        # Initializing a empty Timer
        self.__heartbeat_timer = perpetualTimer(0, lambda: None)
        self.__heartbeat_timer.cancel()
        self.__retry_times = retry_times
        self.__retry_interval = retry_interval
        # in order to compatible with pyinstaller, use if-import instead of importlib.import_module
        if net_type == 'tel':
            from .tel import wifi_portal_login, do_logout
        elif net_type == 'cmcc':
            from .cmcc import wifi_portal_login, do_logout
        else:
            from .unicom import wifi_portal_login, do_logout
        self.__login = lambda: wifi_portal_login(username, password)
        self.__logout = do_logout

    def login(self):
        self.__heartbeat_timer.cancel()
        logging.info('Trying to login the Wi-Fi portal')
        do_heartbeat = None
        login_exception = None
        for i in range(self.__retry_times):
            try:
                do_heartbeat, self.__logout = self.__login()
            except Exception as e:
                login_exception = e
                logging.warning('Portal login failed for {} times'.format(i))
                sleep(self.__retry_interval)
                pass
            else:
                logging.info('Login succeeded')
                break
        if not do_heartbeat:
            logging.error('Login failure for {} times'.format(self.__retry_times))
            raise Exception('Login failure for {} times'.format(self.__retry_times), login_exception)
        self.__heartbeat_timer = perpetualTimer(600, do_heartbeat)
        self.__heartbeat_timer.start()
        return 'Success'

    def logout(self):
        self.cancel_heartbeat()
        self.__logout()
        return 'Success'

    def cancel_heartbeat(self):
        self.__heartbeat_timer.cancel()
        return 'Success'
