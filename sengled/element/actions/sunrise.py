from sengled.element.actions.threaded_action import ThreadedAction


class Sunrise(ThreadedAction):
    def run(self):
        print("Thread Started")

        for device_id in self.home.devices.get_ids():
            self.home.devices.set_color(device_id, 0)

        i = 1
        while not self.event.wait(3) and i < 255:
            for device_id in self.home.devices.get_ids():
                self.home.devices.set_brightness(device_id, i)
            i += 20

        print("Thread Killed")
