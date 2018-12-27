import random

from actions.threaded_action import ThreadedAction


class AwayMode(ThreadedAction):
    def run(self):
        print("Thread Started")
        while not self.event.wait(random.randint(600, 3600)):
            room = random.choice(self.home.rooms[1:])
            room.toggle_state()

        print("Thread Killed")

    def __init__(self, app, endpoint, home, ):
        super().__init__(app, endpoint, home)
