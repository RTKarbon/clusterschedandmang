#!/usr/bin/env python

import subprocess
import shlex, sys, time
from lib import *

def main():
    program_l = ["program1"]
    # flog = open("program_log.txt", 'w')
    flog = sys.stdout
    for pname in program_l:
        cmd = "python ./programs/%s.py" % pname
        proc = subprocess.Popen(shlex.split(cmd), stdout=flog, stderr=flog)
        while proc.returncode == None:
            time.sleep(0.1)
            dbg.print_info("Polling subprocess...")
            proc.poll()
    flog.close()

if __name__ == "__main__":
    main()