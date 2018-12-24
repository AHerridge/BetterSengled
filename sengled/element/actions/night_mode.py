from sengled.element.actions.action import Action


class NightMode(Action):
    def execute(self):
        for device in self.home.devices:
            if self.home.devices.index(device) is 3:
                device.set_color(0)
                device.set_brightness(1)
            else:
                device.set_state(0)

        return "Night Mode"
