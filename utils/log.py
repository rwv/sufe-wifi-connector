import logging
from config import other_config

# logging.basicConfig(level=eval('logging.{}'.format(other_config['log-level'])),
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='log.log',
#                     filemode='w'
#                     )

logging.basicConfig(level=eval('logging.{}'.format(other_config['log-level'])),
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    handlers=[logging.FileHandler('log.log', 'w', 'utf-8')]
                    )
