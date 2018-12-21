from flask import Flask, url_for

from sengled.element import client
from sengled.element.actions.away_mode import AwayMode
from sengled.element.actions.day_mode import DayMode
from sengled.element.actions.night_mode import NightMode
from sengled.element.actions.sunrise import Sunrise


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    home = client.Client("username", "password")
    DayMode(app, home, "dayMode")
    NightMode(app, home, "nightMode")
    Sunrise(app, home, "sunrise")
    AwayMode(app, home, "awayMode", home.devices.get_ids())

    @app.route("/")
    def index():
        links = ""
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and rule.endpoint != "static":
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links += rule.endpoint + " -> <a href=\"" + url + "\">" + url + "</a><br>"
        return links

    return app
