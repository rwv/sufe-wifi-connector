import configparser

cf = configparser.ConfigParser()
cf.read('config.ini', encoding='utf8')

login_config = {
    'type': cf.get('login', 'type'),
    'username': cf.get('login', 'username'),
    'password': cf.get('login', 'password'),
}

other_config = {
    'os': cf.get('other', 'os'),
    'interval': cf.getint('other', 'interval'),
    'retry-times': cf.getint('other', 'retry-times'),
    'retry-interval': cf.getint('other', 'retry-interval'),
    'log-level': cf.get('other', 'log-level')
}


def update_config(data):
    from utils.log import logging
    for section, section_items in data.items():
        for option, value in section_items.items():
            logging.info('Config changed: {}.{}: {}'.format(section, option, value))
            cf.set(section, option, str(value))
    cf.write(open('config.ini', encoding='utf8', mode='w'))
