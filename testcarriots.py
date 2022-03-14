# -*- coding: utf-8 -*-

"""
    Run.py
    Carriots.com
    Created 08 Oct 2016
"""

# !/usr/bin/python
from urllib2 import urlopen, Request
from json import dumps, loads
import json
import androidhelper, time
import datetime
droid=androidhelper.Android()
droid.startLocating()
#import urllib.request
GPIO_pin = 24
ON = 'ON'
OFF = 'OFF'

class Carriots(object):
    api_url = "http://api.carriots.com/"

    def __init__(self, account, api_key, client_type='json'):
        self.client_type = client_type
        self.api_key = api_key
        self.account = account
        self.content_type = "application/vnd.carriots.api.v2+%s" % self.client_type
        self.headers = {'User-Agent': 'Raspberry-Carriots',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type,
                        'Carriots.apikey': self.api_key}
        self.payload = None
        self.response = None

    def set_device(self, device):
        self.device = device + "@" + self.account + "." + self.account

    def send_stream(self, data):
        payload = {"protocol": "v2", "device": self.device, "at": "now", "data": data}
        self.payload = dumps(payload)
        request = Request(self.api_url + "streams", self.payload, self.headers)
        self.response=urlopen(request)
        return json.loads(self.response.read())

    # def get_value_property(self, key_property):
    #     self.payload = None
    #     request = Request(self.api_url + "devices/" + self.device, self.payload, self.headers)
    #     self.response = urlopen(request)
    #     return json.loads(self.response.read()).get("properties").get(key_property)


def main():

    # Carriots parameters
    account = 'madainperez'
    apikey = '56b09de67da15930eb99f882f02b8b62a8f4f0435a5d1fe641827f6a112e577f'
    device = 'arduinotec'
    devicedefault = 'defaultDevice'

    # Instance object Carriots
    carriots = Carriots(account, apikey)
    carriots.set_device(devicedefault)

    history_value_device = OFF

    print
    "\n> :: Welcome...\n"
    for i in range(400):
        now=datetime.datetime.now()
        l=droid.readLocation()
        res=l.result
        print(res)
        try:
        
            lat=res["network"]["latitude"]
            longi=res["network"]["longitude"]
            print(carriots.send_stream({"latitude":lat,"longitude":longi,"fecha":now.year+now.month+now.day,"hora":now.hour+now.minute}))
        except:
            pass
        time.sleep(10)

    # while True:
    #     value_device = carriots.get_value_property('state')  # In this example, we use 'state' text
    #
    #     if value_device != history_value_device:
    #         # if value_device == ON:
    #         #     GPIO.output(GPIO_pin, GPIO.HIGH)
    #         # else:
    #         #     GPIO.output(GPIO_pin, GPIO.LOW)
    #
    #         print
    #         "> Property value of device: " + str(value_device) + "\n"
    #         history_value_device = value_device


if __name__ == '__main__':
    main()

