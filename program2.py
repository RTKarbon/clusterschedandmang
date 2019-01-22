#!/usr/bin/env python

import time
import dbglib as dbg

def program1():
    dbg.print_info("This is hello from program 2")
    time.sleep(1)
    dbg.print_info("This is goodbye from program 2")

if __name__ == "__main__":
    program1()