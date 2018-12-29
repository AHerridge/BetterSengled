import requests

from device import Device
from device import Traits as DeviceTraits
from room import Room
from room import Traits as RoomTraits
from urls import sengled_base_url, zigbee_url, customer_url, room_url, headers


class Client:
    username = None
    password = None
    jsessionid = None
    logged_in = False

    rooms = None
    devices = None

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.load()

    def login(self):
        if self.logged_in:
            return
        print("Logging In")
        login_data = {'os_type': 'android', 'pwd': self.password, 'user': self.username, 'uuid': 'xxxxxx'}
        resp = requests.post(sengled_base_url + zigbee_url + customer_url + 'login.json',
                             headers=headers, verify=False, json=login_data)
        if resp.status_code == 200:
            resp_json = resp.json()
            if 'msg' in resp_json and resp_json['msg'] == 'success':
                headers['Cookie'] = 'JSESSIONID={}'.format(resp_json['jsessionid'])
                self.jsessionid = resp_json['jsessionid']
                self.logged_in = True
            else:
                key = None
                if 'msg' in resp_json:
                    key = 'msg'
                elif 'info' in resp_json:
                    key = 'info'
                if key is not None:
                    print('Login unsuccessful: {}'.format(resp_json[key]))
                    print('Make sure you change the "username" and "password" in /sengled/element/actions/urls.py')
                else:
                    print('Could not login successfully')
        else:
            print('Could not login successfully')

    def load(self):
        self.login()
        print("Loading Devices")
        resp = requests.post(sengled_base_url + zigbee_url + room_url + 'getUserRoomsDetail.json',
                             headers=headers, verify=False, json={})
        if resp.status_code == 200:
            resp_json = resp.json()
            if 'roomList' in resp_json:
                self.parse_room_list(resp_json['roomList'])
        else:
            print('Could not get rooms: {}'.format(resp.status_code))

    def update(self):
        self.login()
        print("Updating Devices")
        # TODO figure out how to get around server delay
        resp = requests.post(sengled_base_url + zigbee_url + room_url + 'getUserRoomsDetail.json',
                             headers=headers, verify=False, json={})
        if resp.status_code == 200:
            resp_json = resp.json()
            if 'roomList' in resp_json:
                for room_data in resp_json['roomList']:
                    room = self.get_room_by_id(room_data[RoomTraits.ID.value])
                    room.data = room_data
                    if 'deviceList' in room_data:
                        for device_data in room_data['deviceList']:
                            device = self.get_device_by_id(device_data[DeviceTraits.ID.value])
                            device.data = device_data
        else:
            print('Could not get rooms: {}'.format(resp.status_code))

    def parse_room_list(self, room_list):
        self.devices = []
        self.rooms = []

        for room_data in room_list:
            devices = []
            if 'deviceList' in room_data:
                for device_data in room_data['deviceList']:
                    device = Device(device_data, self)
                    devices.append(device)
                    self.devices.append(device)
            self.rooms.append(Room(room_data, devices))

    def get_room_by_id(self, room_id):
        for room in self.rooms:
            if int(room.get_id()) == int(room_id):
                return room
        print("Room not found:", room_id)
        return None

    def get_device_by_id(self, device_id):
        for device in self.devices:
            if device.get_id() == device_id:
                return device
        print("Device not found:", device_id)
        return None

    def get_room_for_device(self, device):
        for room in self.rooms:
            if device in room.devices:
                return room
        print("Room not found for device:", device.get_id())
        return None
