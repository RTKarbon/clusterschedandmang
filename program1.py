#!/usr/bin/env python

import time
from lib import *

def program1():
    dbg.print_info("This is hello from program 1")
    dbg.print_info("Program 1 is working...")
    time.sleep(1)
    dbg.print_info("This is goodbye from program 1")

if __name__ == "__main__":
    program1()