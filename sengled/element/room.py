from sengled.element.device import Device


class Room:
    devices = []
    data = None

    def __init__(self, data):
        self.data = data

        for device_data in data['deviceList']:
            self.add_device(Device(device_data))

    def add_device(self, device):
        device.set_device_value('roomId', self.data['room_id'])
        self.devices.append(device)

    def clear_device_list(self):
        self.devices = []

    def get_devices(self):
        return self.devices
