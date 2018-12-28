class Action:
    home = None

    def execute(self):
        print("Not Implemented Yet!")

    def __init__(self, app, endpoint, home):
        rule = "/actions/" + endpoint
        print("Creating endpoint :", rule)
        app.add_url_rule(rule, endpoint, self.execute)
        self.home = home
