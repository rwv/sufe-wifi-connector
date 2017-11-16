from subprocess import check_output
import re


def get_wifi_ssid():
    results = check_output(["netsh", "wlan", "show", "interfaces"], shell=True).decode('gbk')
    ssid = re.findall('SSID\s*: (.*)\r\n', results)[0]
    return ssid
