import random

from sengled.element.actions.threaded_action import ThreadedAction


class AwayMode(ThreadedAction):
    devices = None

    def run(self):
        print("Thread Started")
        while not self.event.wait(1):
            device = random.choice(self.devices)
            device.toggle_state()

        print("Thread Killed")

    def __init__(self, app, endpoint, home, devices):
        super().__init__(app, endpoint, home)
        self.devices = devices
