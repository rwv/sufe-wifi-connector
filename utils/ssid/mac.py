import re
import subprocess

from utils.log import logging


def get_wifi_ssid():
    """
    get wifi ssid in mac system
    by executing "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I"

    :return: the first ssid of mac wlan and '' if failed to fetch
    """
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
