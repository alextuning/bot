#!/usr/bin/python
import serial
import sys

action = sys.argv[1]
port = serial.Serial('/dev/ttyACM0', 9600)
#print('heater ' + action)
port.write('heater ' + action)
port.close()
