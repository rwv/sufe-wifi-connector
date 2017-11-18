import re
import subprocess
from utils.log import logging


def get_wifi_ssid():
    result = subprocess.run(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'],
        stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    logging.debug(
        '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I\n{}'.format(
            result))
    ssid = re.search(' SSID: (.*)\n', result)
    if ssid:
        ssid = ssid.group(1)
    else:
        ssid = ''
    return ssid
