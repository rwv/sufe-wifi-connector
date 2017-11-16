import configparser

cf = configparser.ConfigParser()
cf.read('config.ini')

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
