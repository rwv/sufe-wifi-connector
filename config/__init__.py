import configparser

cf = configparser.ConfigParser()
cf.read('config.ini', encoding='utf8')

login_config = {
    'network_type': cf.get('login', 'network_type'),
    'username': cf.get('login', 'username'),
    'password': cf.get('login', 'password'),
}

other_config = {
    'os': cf.get('other', 'os'),
    'detect_interval': cf.getint('other', 'detect_interval'),
    'retry_times': cf.getint('other', 'retry_times'),
    'retry_interval': cf.getint('other', 'retry_interval'),
    'log_level': cf.get('other', 'log_level')
}


def update_config(data):
    from utils.log import logging
    for section, section_items in data.items():
        for option, value in section_items.items():
            logging.info('Config changed: {}.{}: {}'.format(section, option, value))
            cf.set(section, option, str(value))
    cf.write(open('config.ini', encoding='utf8', mode='w'))
