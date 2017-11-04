import re
import subprocess


def get_wifi_ssid():
    result = subprocess.run(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'],
        stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    ssid = re.search(' SSID: (.*)\n', result)
    if ssid:
        ssid = ssid.group(1)
    else:
        ssid = ''
    return ssid
