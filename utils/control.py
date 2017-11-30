import config
import utils.connector
import utils.log
from model import Wifi
from utils.ssid import SSID
from utils.test_connection import test_connection

ssid = SSID(config.other_config['os'], config.login_config['network_type'])
wifi = Wifi(config.login_config['username'], config.login_config['password'], config.login_config['network_type'],
            config.other_config['retry_times'], config.other_config['retry_interval'])
connector = utils.connector.Connector(ssid, wifi, config.other_config['detect_interval'])


def start():
    utils.log.logging.info('Service started')
    try:
        connector.start()
        return 'Success'
    except Exception as e:
        return 'Error: {}'.format(str(e))


def stop():
    utils.log.logging.info('Service stopped')
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
        reload()
        return 'Success'
    except Exception as e:
        return 'Error: {}'.format(str(e))


def get_config():
    return {'login': config.login_config,
            'other': config.other_config}


def get_log():
    return utils.log.get_log()


def reload():
    utils.log.logging.info('Service reloaded')
    global connector
    if connector.status:
        connector.stop()
        ssid = SSID(config.other_config['os', config.login_config['network_type']])
        wifi = Wifi(config.login_config['username'], config.login_config['password'],
                    config.login_config['network_type'],
                    config.other_config['retry_times'], config.other_config['retry_interval'])
        connector = utils.connector.Connector(ssid, wifi, config.other_config['detect_interval'])
        connector.start()
    else:
        ssid = SSID(config.other_config['os', config.login_config['network_type']])
        wifi = Wifi(config.login_config['username'], config.login_config['password'],
                    config.login_config['network_type'],
                    config.other_config['retry_times'], config.other_config['retry_interval'])
        connector = utils.connector.Connector(ssid, wifi, config.other_config['detect_interval'])
