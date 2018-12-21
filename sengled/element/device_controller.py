from enum import Enum

import requests

from sengled.element import sengled_base_url, zigbee_url, device_url


class Traits(Enum):
    BRIGHTNESS = ['Brightness', 'brightness']  # 0-255
    COLOR_TEMP = ['ColorTemperature', 'colorTemperature']  # 0-100
    STATE = ['OnOff', 'onoff']  # ON=1 OFF=0
    NAME = ['DeviceName', 'deviceName']
    ID = ['DeviceId', 'deviceUuid']


class DeviceController:
    devices = None
    client = None

    def add_device(self, device, room_id):
        device['roomId'] = room_id
        self.devices.append(device)

    def clear_device_list(self):
        self.devices = []

    def get_names(self):
        device_names = []
        for device in self.devices:
            device_names.append(device[Traits.NAME.value[1]])
        return device_names

    def get_ids(self):
        device_ids = []
        for device in self.devices:
            device_ids.append(device[Traits.ID.value[1]])
        return device_ids

    def get_device_id(self, device_name):
        for device in self.devices:
            if Traits.NAME.value[1] in device and device[Traits.NAME.value[1]] == device_name and Traits.ID.value[
                1] in device:
                return device[Traits.ID.value[1]]
        return None

    def get_device(self, device_id):
        for device in self.devices:
            if device[Traits.ID.value[1]] == device_id:
                return device

    def update_value(self, device_id, name, value):
        self.get_device(device_id)[name] = value

    def set_device_value(self, device_id, key, value):
        self.client.login()
        toggle_json = {Traits.ID.value[1]: device_id, key.value[1]: value}
        url = sengled_base_url + zigbee_url + device_url + 'deviceSet' + key.value[0] + '.json'
        print(self.get_device(device_id)[Traits.NAME.value[1]] + "." + key.name, "->", value)
        resp = requests.post(url, headers=self.client.headers, json=toggle_json, verify=False)
        if resp.status_code == 200:
            self.update_value(device_id, key.value[1], value)
            return True
        else:
            print('Could not change device value: ' + resp.reason)
            return False

    def set_brightness(self, device_id, value):
        return self.set_device_value(device_id, Traits.BRIGHTNESS, value)

    def set_color(self, device_id, value):
        return self.set_device_value(device_id, Traits.COLOR_TEMP, value)

    def set_state(self, device_id, value):
        return self.set_device_value(device_id, Traits.STATE, value)

    def toggle_state(self, device_id):
        device = self.get_device(device_id)
        self.set_state(device_id, 0 if device[Traits.STATE.value[1]] else 1)

    def __init__(self, client):
        self.devices = []
        self.client = client
