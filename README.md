![Demo Image](https://i.imgur.com/NWJmQB1.png)

# Flask-based Sengled Interface
[flask](http://flask.pocoo.org/): to provide web endpoints for easy automation using IFTTT etc.

[sengled-python](https://github.com/sroehl/sengled-python): to interface with the Sengled Element api

## Devices Tested
* [Element Classic](https://us.sengled.com/products/element-classic-bulb) (Dimmable)
* [Element Plus](https://us.sengled.com/products/element-plus-bulb) (Dimmable, Tunable White)

## Getting Started
**You must change the "username" and "password" in setup.py**

In console type:

```sh
export FLASK_APP=setup.py
export FLASK_ENVIRONMENT=development
flask run
```

Open in web browser - default: [localhost:5000/home](http://localhost:5000/home)

**See actions for advanced examples of how to use the library to control Sengled Element bulbs.**

## API Endpoints
- /devices -> get all devices as json list
- /devices/<device_id> -> get data for device identified by device_id as json
- /devices/<device_id>/<trait_name>/<new_value> -> set device trait to value and return "Success" or "Failure"
- /rooms -> get all rooms as json list
- /rooms/<room_id> -> get data for room identified by room_id as json
- /rooms/<room_id>/<trait_name>/<new_value> -> set room trait to value and return "Success" or "Failure"
- /actions/<action_name> -> executes action

Device traits are defined in devices.py
Room traits are defined in rooms.py
