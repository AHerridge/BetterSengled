from enum import Enum

from sengled.element.device import Device


class Traits(Enum):
    BRIGHTNESS = 'brightness'  # 0-255
    COLOR_TEMP = 'colortemperature'  # 0-100
    STATUS = 'roomStatus'  # ON=1 OFF=0
    NAME = 'roomName'
    ID = 'roomId'
    COLOR_R = 'rgbColorR'  # 0-255
    COLOR_G = 'rgbColorG'  # 0-255
    COLOR_B = 'rgbColorB'  # 0-255
    IMG_TYPE = 'roomImgType'
    IMG_URL = 'roomImgUrl'

    def to_pascal_case(self):
        if self is Traits.COLOR_TEMP:
            return 'ColorTemperature'
        else:
            return self.value[:1].upper() + self.value[1:]


class Room:
    devices = []
    data = None

    def __init__(self, data):
        self.data = data

        for device_data in data['deviceList']:
            self.add_device(Device(device_data))

    def add_device(self, device):
        self.devices.append(device)

    def clear_device_list(self):
        self.devices = []

    def get_devices(self):
        return self.devices

    def get_trait(self, trait):
        return self.data[trait.value]
