#!/usr/bin/python
#-*- encoding: utf-8 -*-
import argparse
import time
from mcp23017 import mcp23017

if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--device', help="device file name", default='/dev/i2c-1')
        parser.add_argument('-a', '--addr', type=lambda x: int(x, 16), help="i2c address", default=0x20)
        parser.add_argument('--delay', type=float, help="Delay time", default=0.1)
        args = parser.parse_args()

        mcp = mcp23017(args.device, args.addr)
        # Set GPX as output
        for i in range(8):
                print("Set GP{} as output".format(i))
                mcp.setup(i, 'OUT', 'A')
                mcp.setup(i, 'OUT', 'B')
        while True:
                for i in range(8):
                        mcp.output(i, 1, 'A')
                        time.sleep(args.delay)
                        mcp.output(i, 0, 'A')
                for i in range(8):
                        mcp.output(i, 1, 'B')
                        time.sleep(args.delay)
                        mcp.output(i, 0, 'B')
