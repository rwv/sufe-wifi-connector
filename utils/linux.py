from subprocess import check_output
from utils.log import logging


def get_wifi_ssid():
    scan_output = check_output(["iwlist", "wlan0", "scan"])
    ssid = ''
    logging.debug('iwlist wlan0 scan\n'.format(scan_output))
    for line in scan_output.split():
        if line.startswith("ESSID"):
            ssid = line.split('"')[1]
            break
    return ssid
