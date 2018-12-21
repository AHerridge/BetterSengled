import random

from sengled.element.actions.threaded_action import ThreadedAction


class AwayMode(ThreadedAction):
    devices = None

    def run(self):
        print("Thread Started")
        while not self.event.wait(1):
            device_id = random.choice(self.devices)
            self.home.devices.toggle_state(device_id)

        print("Thread Killed")

    def __init__(self, app, home, endpoint, devices):
        super().__init__(app, home, endpoint)
        self.devices = devices
