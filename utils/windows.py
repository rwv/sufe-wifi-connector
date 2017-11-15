from subprocess import check_output
import re


def get_wifi_ssid():
    result = check_output(["netsh", "wlan", "show", "network"])
    result = result.decode("gbk")
    ssid = re.findall('SSID\s+: (.*) \n', result)[0]
    return ssid
