from enum import Enum

import requests

from sengled.element import sengled_base_url, zigbee_url, device_url, headers


class Traits(Enum):
    BRIGHTNESS = ['Brightness', 'brightness']  # 0-255
    COLOR_TEMP = ['ColorTemperature', 'colorTemperature']  # 0-100
    STATE = ['OnOff', 'onoff']  # ON=1 OFF=0
    NAME = ['DeviceName', 'deviceName']
    ID = ['DeviceId', 'deviceUuid']


class Device:
    data = None

    def __init__(self, data):
        self.data = data

    def set_device_value(self, key, value):
        toggle_json = {Traits.ID.value[1]: self.get_id(), key.value[1]: value}
        url = sengled_base_url + zigbee_url + device_url + 'deviceSet' + key.value[0] + '.json'
        print(self.get_name() + "." + key.name, "->", value)
        resp = requests.post(url, headers=headers, json=toggle_json, verify=False)
        if resp.status_code == 200:
            self.data[key.value[1]] = value
            return True
        else:
            print('Could not change device value: ' + resp.reason)
            return False

    def set_brightness(self, value):
        return self.set_device_value(Traits.BRIGHTNESS, value)

    def set_color(self, value):
        return self.set_device_value(Traits.COLOR_TEMP, value)

    def set_state(self, value):
        return self.set_device_value(Traits.STATE, value)

    def toggle_state(self):
        self.set_state(0 if self.get_state() else 1)

    def get_state(self):
        return self.data[Traits.STATE.value[1]]

    def get_name(self):
        return self.data[Traits.NAME.value[1]]

    def get_id(self):
        return self.data[Traits.ID.value[1]]
