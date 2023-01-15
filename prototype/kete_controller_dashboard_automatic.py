#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

cred = credentials.Certificate('/home/pi/kete-smart-gardening-da5be-firebase-adminsdk-kaev2-cf6e001642.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kete-smart-gardening-da5be-default-rtdb.europe-west1.firebasedatabase.app/'
})

__all__ = ["GroveMoistureSensor", "GroveRelay"]


class GroveMoistureSensor:
    '''
    Grove Moisture Sensor class

    Args:
        pin(int): number of analog pin/channel the sensor connected.
    '''

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def moisture(self):
        '''
        Get the moisture strength value/voltage

        Returns:
            (int): voltage, in mV
        '''
        value = self.adc.read_voltage(self.channel)
        return value


Grove = GroveMoistureSensor


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

def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = 0 #sh.argv2pin()

    sensor = GroveMoistureSensor(pin)
    relay = GroveRelay(12)
    
    print('Detecting moisture...')
    while True:
        print('1')
        m = sensor.moisture
        if 0 <= m and m < 300:
            result = 'Trochen'
            try:
                relay.on()
                print("Es wird bewässert!")
                time.sleep(2)
                relay.off()
            except KeyboardInterrupt:
                relay.off()
                print("exit")
                exit(1)            
        elif 300 <= m and m < 600:
            result = 'Feucht'
        else:
            result = 'Nass'
        print('Moisture value: {0}, {1}'.format(m, result))
        current_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        soilMoisturePercent = (m / 2200) * 100
        print(soilMoisturePercent)
        data = {
            'sensor_id': 10000,
            'sensor_name': "Sensor 1",
            'sensor_type': "moisture",
            'time': current_time,
            'value': soilMoisturePercent,
            'value_type': '%',
            'user_id' : 1465214
        }

        json_data = json.dumps(data)
        print(json_data)
        db.reference('sensors/sensor_data').push(json_data)
        time.sleep(1)


if __name__ == '__main__':
    main()

