#!/usr/bin/env python

import time
from common import *

def program2():
    dbg.print_info("This is hello from program 2")
    dbg.print_info("Program 2 is working...")
    time.sleep(1)
    dbg.print_info("This is goodbye from program 2")

if __name__ == "__main__":
    program1()