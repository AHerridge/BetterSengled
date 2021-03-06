from flask import Flask, url_for, render_template, jsonify

import client
import device
import room
from actions.away_mode import AwayMode
from actions.day_mode import DayMode
from actions.night_mode import NightMode
from actions.sunrise import Sunrise


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["JSON_AS_ASCII"] = False
    home = client.Client("username", "password")  # <-- CHANGE THIS LINE
    DayMode(app, "dayMode", home)
    NightMode(app, "nightMode", home)
    Sunrise(app, "sunrise", home)
    AwayMode(app, "awayMode", home)

    @app.route("/")
    def index():
        links = ""
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and rule.endpoint != "static":
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links += rule.endpoint + " -> <a href=\"" + url + "\">" + url + "</a><br>"
        return links

    @app.route("/home")
    def home_page():
        home.update()
        return render_template("home.html", RoomTraits=room.Traits, DeviceTraits=device.Traits, rooms=home.rooms)

    @app.route("/devices")
    def get_devices():
        return jsonify([device.data for device in home.devices])

    @app.route("/devices/<device_id>")
    def get_device(device_id):
        return jsonify(home.get_device_by_id(device_id).data)

    @app.route("/devices/<device_id>/<trait_name>")
    def get_device_trait(device_id, trait_name):
        return home.get_device_by_id(device_id).get_trait(device.Traits[trait_name])

    @app.route("/devices/<device_id>/<trait_name>/<value>")
    def set_device_trait(device_id, trait_name, value):
        return "Success" if home.get_device_by_id(device_id).set_trait(device.Traits[trait_name], value) else "Failure"

    @app.route("/rooms")
    def get_rooms():
        return jsonify([room.data for room in home.rooms])

    @app.route("/rooms/<room_id>")
    def get_room(room_id):
        return jsonify(home.get_room_by_id(room_id).data)

    @app.route("/rooms/<room_id>/<trait_name>")
    def get_room_trait(room_id, trait_name):
        return home.get_room_by_id(room_id).get_trait(room.Traits[trait_name])

    @app.route("/rooms/<room_id>/<trait_name>/<value>")
    def set_room_trait(room_id, trait_name, value):
        return "Success" if home.get_room_by_id(room_id).set_trait(room.Traits[trait_name], value) else "Failure"

    return app
