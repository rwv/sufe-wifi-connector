import config
import utils.log
import utils.connector
from utils.test_connection import test_connection
from utils.ssid import SSID

ssid = SSID(config.other_config['os'])
connector = utils.connector.Connector()


def start():
    try:
        connector.start()
        return 'Success'
    except Exception as e:
        return 'Error: {}'.format(str(e))



def stop():
    try:
        connector.stop()
        return 'Success'
    except Exception as e:
        return 'Error: {}'.format(str(e))


def get_status():
    result = {
        "service_status": "Running" if connector.status else "Stopped",
        "internet_connection": "Online" if test_connection() else "Offline",
        "network_type": config.login_config['network_type'],
        "ssid": ssid.get()
    }
    return result


def update_config(data):
    try:
        config.update_config(data)
        connector.reload()
        return 'Success'
    except Exception as e:
        return 'Error: {}'.format(str(e))


def get_config():
    return {'login': config.login_config,
            'other': config.other_config}


def get_log():
    return utils.log.get_log()
