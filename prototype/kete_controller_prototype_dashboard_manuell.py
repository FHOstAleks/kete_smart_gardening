#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import math
import sys
import time
import datetime
import json
from grove.adc import ADC
from grove.gpio import GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, request
from flask_cors import CORS

class GroveRelay(GPIO):
    '''
    Class for Grove - Relay

    Args:
        pin(int): number of digital pin the relay connected.
    '''
    def __init__(self, pin):
        super(GroveRelay, self).__init__(pin, GPIO.OUT)

    def on(self):
        '''
        enable/on the relay
        '''
        self.write(1)

    def off(self):
        '''
        disable/off the relay
        '''
        self.write(0)


Grove = GroveRelay

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['POST'])
def receive_data():
    print(request.get_json())
    data = request.get_json()
    print(data)
    sensor_id = data.get('sensor_id')
    sensor_name = data.get('sensor_name')
    user_id = data.get('user_id')
    action = data.get('action')
    # handle the received data here
    print(f"Received data: Sensor ID: {sensor_id}, Sensor Name: {sensor_name}, User ID: {user_id}, Action: {action}")
    relay = GroveRelay(12)
    
    if action == 'start':
        relay.on()
        return "Bewässerung gestartet"
    
    if action == 'stop':
        relay.off()
        return "Bewässerung beendet"
    

if __name__ == '__main__':
    # host 0.0.0.0 ermöglicht es im lokalen Netzwerk verfügbar zu sein
    app.run(host='0.0.0.0', port=5000)


