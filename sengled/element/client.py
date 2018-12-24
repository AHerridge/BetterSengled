import requests

from sengled.element import sengled_base_url, zigbee_url, customer_url, room_url, headers
from sengled.element.device import Device
from sengled.element.room import Room


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
        self.devices = []
        self.rooms = []
        self.update()

    def login(self):
        if self.logged_in:
            return
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
                    print('Make sure you change the "username" and "password" in /sengled/element/actions/__init__.py')
                else:
                    print('Could not login successfully')
        else:
            print('Could not login successfully')

    def update(self):
        self.login()
        resp = requests.post(sengled_base_url + zigbee_url + room_url + 'getUserRoomsDetail.json',
                             headers=headers, verify=False, json={})
        if resp.status_code == 200:
            resp_json = resp.json()
            if 'roomList' in resp_json:
                self.parse_room_list(resp_json['roomList'])
        else:
            print('Could not get rooms: {}'.format(resp.status_code))

    def parse_room_list(self, room_list):
        for room_data in room_list:
            if 'deviceList' in room_data:
                for device_data in room_data['deviceList']:
                    self.devices.append(Device(device_data))
            self.rooms.append(Room(room_data))
