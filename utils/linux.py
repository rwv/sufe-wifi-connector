from subprocess import check_output


def get_wifi_ssid():
    scan_output = check_output(["iwlist", "wlan0", "scan"])
    ssid = ''
    for line in scan_output.split():
        if line.startswith("ESSID"):
            ssid = line.split('"')[1]
            break
    return ssid
