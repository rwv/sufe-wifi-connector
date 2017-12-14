from subprocess import check_output

from utils.log import logging


def get_wifi_ssid():
    """
    get wifi ssid in linux system
    by executing "iwlist wlan0 scan"

    :return: the first ssid of linux wlan
    """
    scan_output = check_output(["iwlist", "wlan0", "scan"]).decode()
    ssid = ''
    logging.debug('iwlist wlan0 scan\n'.format(scan_output))
    for line in scan_output.split():
        if line.startswith("ESSID"):
            ssid = line.split('"')[1]
            break
    return ssid
