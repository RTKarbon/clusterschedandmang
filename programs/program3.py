#!/usr/bin/env python

import time
from common import *

def program3():
    dbg.print_info("This is hello from program 3")
    dbg.print_info("Program 3 is working...")
    time.sleep(2)
    dbg.print_info("This is goodbye from program 3")

if __name__ == "__main__":
    program3()