from sengled.element.actions.action import Action


class DayMode(Action):
    def execute(self):
        for room in self.home.rooms:
            room.set_color(50)
            room.set_brightness(128)

        return "Day Mode"
