import objc


def get_wifi_interface():
    objc.loadBundle('CoreWLAN',
                    bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                    module_globals=globals())
    interfaces = []
    for iname in CWInterface.interfaceNames():
        interface = CWInterface.interfaceWithName_(iname)
    interfaces.append({
        'interface': iname,
        'ssid': interface.ssid(),
        'transmit_rate': interface.transmitRate(),
        'transmit_power': interface.transmitPower(),
        'rssi': interface.rssi()
    })
    return interfaces
