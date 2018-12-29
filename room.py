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

    def set_trait(self, trait, value):
        print(self.get_name() + "." + trait.name, self.get_trait(trait), "->", value)
        if trait is Traits.BRIGHTNESS:
            self.set_brightness(value)
        elif trait is Traits.COLOR_TEMP:
            self.set_color_temp(value)
        elif trait is Traits.STATUS:
            self.set_state(value)
        else:
            print("Set room", trait.name, "not implemented yet")

        self.data[trait.value] = value

    def set_brightness(self, value):
        for device in self.devices:
            device.set_brightness(value)
        self.update_status()

    def set_color_temp(self, value):
        for device in self.devices:
            device.set_color_temp(value)

    def set_state(self, value):
        for device in self.devices:
            device.set_state(value)
        self.update_status()

    def toggle_state(self):
        value = 0 if self.get_trait(Traits.STATUS) else 1
        for device in self.devices:
            device.set_state(value)

        self.data[Traits.STATUS.value] = value
        self.update_status()

    def update_status(self):
        status = 0
        for device in self.devices:
            if device.get_state() == 1:
                status = 1
                break

        self.data[Traits.STATUS.value] = status


def gen_getter(trait):
    getter_name = 'get_' + trait.to_snake_case()

    def getter(self):
        return self.get_trait(trait)

    setattr(Room, getter_name, getter)


def gen_getters():
    for trait in Traits:
        gen_getter(trait)


gen_getters()
