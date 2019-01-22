#!/usr/bin/env python

import subprocess
import shlex
from lib import *

def main():
    proc = subprocess.Popen(shlex.split("python ./programs/program1.py"))
    # Try comment out next line
    # proc.wait()

if __name__ == "__main__":
    main()