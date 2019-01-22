#!/usr/bin/env python

import subprocess
import shlex
from lib import *

def main():
    program_l = ["program1", "program2", "program3"]
    proc_l = list()
    # Launch processes
    for pname in program_l:
        cmd = "python ./programs/%s.py" % pname
        proc = subprocess.Popen(shlex.split(cmd))
        proc_l.append(proc)
    # Wait for all processes to finish
    for proc in proc_l:
        proc.wait()

if __name__ == "__main__":
    main()