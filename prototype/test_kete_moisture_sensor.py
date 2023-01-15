#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Für Testzwecke
import math
import sys
import time
import datetime
import json
from grove.adc import ADC
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/home/pi/kete-smart-gardening-da5be-firebase-adminsdk-kaev2-cf6e001642.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kete-smart-gardening-da5be-default-rtdb.europe-west1.firebasedatabase.app/'
})

__all__ = ["GroveMoistureSensor"]

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

def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = sh.argv2pin()

    sensor = GroveMoistureSensor(pin)
    
    print('Detecting moisture...')
    while True:
        m = sensor.moisture
        if 0 <= m and m < 300:
            result = 'Dry'
        elif 300 <= m and m < 600:
            result = 'Moist'
        else:
            result = 'Wet'
        print('Moisture value: {0}, {1}'.format(m, result))
        current_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        soilMoisturePercent = (m/2200) * 100
        print(soilMoisturePercent)
        data = {
            'sensor_id': 10000,
            'sensor_name': "Sensor 1",
            'sensor_type': "moisture",
            'time': current_time,
            'value': m,
            'percent': soilMoisturePercent
        }
        
        json_data = json.dumps(data)
        print(json_data)
        db.reference('sensors/sensor_data').push(json_data)
        time.sleep(1)

if __name__ == '__main__':
    main()
