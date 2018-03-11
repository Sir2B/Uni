#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, rrdtool, time
import Adafruit_DHT

# function: read and parse sensor data file
def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except (IOError), e:
    print time.strftime("%x %X"), "Error reading", path, ": ", e
  return value

# define pathes to 1-wire sensor data
pathes = (
  "/sys/bus/w1/devices/28-00000581ac32/w1_slave",
  "/sys/bus/w1/devices/28-00044e6f1eff/w1_slave"
)

# read sensor data
data = 'N'
for path in pathes:
  data += ':'
  data += read_sensor(path)
  time.sleep(1)
  
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)
data += ':{}:{}'.format(temperature, humidity)

# rrdtool create values.rrd --step 300 DS:temp0:GAUGE:600:-40:100 DS:temp1:GAUGE:600:-40:100 DS:temp2:GAUGE:600:-40:100 DS:humidity0:GAUGE:600:-1:101 RRA:AVERAGE:0.5:1:576 RRA:AVERAGE:0.5:12:336 RRA:AVERAGE:0.5:288:365 RRA:AVERAGE:0.5:8640:600

# insert data into round-robin-database
rrdtool.update(
  "%s/values.rrd" % (os.path.dirname(os.path.abspath(__file__))),
  data)
