from sengled.element.actions.action import Action


class DayMode(Action):
    def execute(self):
        for device_id in self.home.devices.get_ids():
            self.home.devices.set_color(device_id, 50)
            self.home.devices.set_brightness(device_id, 128)

        return "Day Mode"
