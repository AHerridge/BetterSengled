class Action:
    home = None

    def execute(self):
        print("Not Implemented Yet!")

    def toggle_state(self, device_id):
        return self.home.devices.toggle_state(device_id)

    def __init__(self, app, home, endpoint):
        rule = "/" + endpoint
        print("Creating endpoint :", rule)
        app.add_url_rule(rule, endpoint, self.execute)
        self.home = home
