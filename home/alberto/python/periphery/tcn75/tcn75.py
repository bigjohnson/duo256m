#!/usr/bin/python
#modify from https://github.com/paavoleinonen/tcn75a
#-*- encoding: utf-8 -*-
import argparse
import time
from periphery import I2C
device = I2C('/dev/i2c-1')
msgs = [I2C.Message([0x00]), I2C.Message([0,0], read=True)]
device.transfer(0x4f, msgs)
temp = ((msgs[1].data[0] * 256) + (msgs[1].data[1] & 0xF0)) / 16
if temp > 2047 :
  temp -= 4096
cTemp = temp  * 0.0625
fTemp = (cTemp * 1.8) + 32
print(cTemp)
