import config
import utils.log
import utils.connector

connector = utils.connector.Connector()


def start():
    connector.start()
    return 'Success'


def stop():
    connector.stop()
    return 'Success'


def status():
    return connector.status


def update_config(data):
    config.update_config(data)
    connector.reload()
    return 'Success'


def get_config():
    return {'login': config.login_config,
            'other': config.other_config}


def get_log():
    return utils.log.get_log()
