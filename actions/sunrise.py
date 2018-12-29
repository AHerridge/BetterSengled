from actions.threaded_action import ThreadedAction


class Sunrise(ThreadedAction):
    def run(self):
        print("Thread Started")

        for room in self.home.rooms:
            room.set_color_temp(0)

        i = 1
        while not self.event.wait(3) and i < 255:
            for room in self.home.rooms:
                room.set_brightness(i)
            i += 20

        print("Thread Killed")
