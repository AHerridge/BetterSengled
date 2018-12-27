import threading

from actions.action import Action


class ThreadedAction(Action):
    thread = None
    event = None

    def execute(self):
        if self.thread is None or not self.thread.isAlive():
            self.event = threading.Event()
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
            return "On"
        else:
            self.event.set()
            self.thread.join()
            return "Off"

    def run(self):
        print("Not Implemented Yet!")
