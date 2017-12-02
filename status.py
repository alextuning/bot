#!/usr/bin/python
import serial
import time

port = serial.Serial('/dev/ttyACM0',9600,timeout=1)
port.write("get temp")
time.sleep(3)
port.write("status")
time.sleep(3)
st = port.read(size=256)
port.close()
file = open("/tmp/status.txt","w")
file.write(st)
