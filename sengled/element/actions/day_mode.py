from sengled.element.actions.action import Action


class DayMode(Action):
    def execute(self):
        for device in self.home.devices:
            device.set_color(50)
            device.set_brightness(128)

        return "Day Mode"
