from enum import Enum


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

    def to_snake_case(self):
        return self.name.lower()


class Room:
    devices = None
    data = None

    def __init__(self, data, devices):
        self.data = data
        self.devices = devices

    def add_device(self, device):
        self.devices.append(device)

    def clear_device_list(self):
        self.devices = []

    def get_devices(self):
        return self.devices

    def get_trait(self, trait):
        return self.data[trait.value]

    def set_brightness(self, value):
        for device in self.devices:
            device.set_brightness(value)

    def set_color(self, value):
        for device in self.devices:
            device.set_color(value)

    def set_state(self, value):
        for device in self.devices:
            device.set_state(value)

    def toggle_state(self):
        value = 0 if self.get_trait(Traits.STATUS) else 1
        for device in self.devices:
            device.set_state(value)

        self.data[Traits.STATUS.value] = value


def gen_getter(trait):
    getter_name = 'get_' + trait.to_snake_case()

    def getter(self):
        return self.get_trait(trait)

    setattr(Room, getter_name, getter)


def gen_getters():
    for trait in Traits:
        gen_getter(trait)


gen_getters()
