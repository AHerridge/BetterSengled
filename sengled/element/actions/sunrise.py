from sengled.element.actions.threaded_action import ThreadedAction


class Sunrise(ThreadedAction):
    def run(self):
        print("Thread Started")

        for device in self.home.devices:
            device.set_color(0)

        i = 1
        while not self.event.wait(3) and i < 255:
            for device in self.home.devices:
                device.set_brightness(i)
            i += 20

        print("Thread Killed")
