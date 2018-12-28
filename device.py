from enum import Enum

import requests

from urls import sengled_base_url, zigbee_url, device_url, headers


class Traits(Enum):
    BRIGHTNESS = 'brightness'  # 0-255
    COLOR_TEMP = 'colorTemperature'  # 0-100
    STATE = 'onoff'  # ON=1 OFF=0

    #  NOT SURE IF SET WORKS FOR THESE
    NAME = 'deviceName'
    ID = 'deviceUuid'
    GATEWAY_ID = 'gatewayUuid'
    SIGNAL_QUALITY = 'signalQuality'
    SIGNAL_VALUE = 'signalValue'
    ACTIVE_HOURS = 'activeHours'
    ONLINE = 'isOnline'  # ON=1 OFF=0
    POWER = 'power'
    ON_COUNT = 'onCount'
    POWER_CONSUMPTION_TIME = 'powerConsumptionTime'
    PRODUCT_CODE = 'productCode'
    ATTRIBUTE_IDS = 'attributeIds'  # Comma-separated list of integers
    COLOR_R = 'rgbColorR'  # 0-255
    COLOR_G = 'rgbColorG'  # 0-255
    COLOR_B = 'rgbColorB'  # 0-255

    def to_pascal_case(self):
        if self is Traits.STATE:
            return 'OnOff'
        elif self is Traits.COLOR_TEMP:
            return 'ColorTemperature'
        else:
            return self.value[:1].upper() + self.value[1:]


class Device:
    data = None
    home = None

    def __init__(self, data, home):
        self.data = data
        self.home = home

    def set_trait(self, trait, value):
        toggle_json = {Traits.ID.value: self.get_trait(Traits.ID), trait.value: value}
        url = sengled_base_url + zigbee_url + device_url + 'deviceSet' + trait.to_pascal_case() + '.json'
        print(self.get_trait(Traits.NAME) + "." + trait.name, self.get_trait(trait), "->", value)
        resp = requests.post(url, headers=headers, json=toggle_json, verify=False)
        if resp.status_code == 200:
            if trait.value in self.data:
                if trait is Traits.COLOR_TEMP:
                    self.data[trait.value.lower()] = int(value)
                elif str(self.data[trait.value]).isdigit():
                    self.data[trait.value] = int(value)
                else:
                    self.data[trait.value] = value
            # self.home.update() unnecessary because of server delay
            return True
        else:
            print('Could not change device value: ' + resp.reason)
            return False

    def set_brightness(self, value):
        return self.set_trait(Traits.BRIGHTNESS, value)

    def set_color(self, value):
        return self.set_trait(Traits.COLOR_TEMP, value)

    def set_state(self, value):
        return self.set_trait(Traits.STATE, value)

    def toggle_state(self):
        self.set_state(0 if self.get_trait(Traits.STATE) else 1)

    def get_trait(self, trait):
        if trait.value in self.data:
            return self.data[trait.value]
        elif trait is Traits.COLOR_TEMP:
            return self.data[trait.value.lower()]
        else:
            return "N/A"
