from sengled.element.actions.action import Action


class NightMode(Action):
    def execute(self):
        for device_id in self.home.devices.get_ids():
            if self.home.devices.get_ids().index(device_id) is 3:
                self.home.devices.set_color(device_id, 0)
                self.home.devices.set_brightness(device_id, 1)
            else:
                self.home.devices.set_state(device_id, 0)

        return "Night Mode"
