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
        time.sleep(0.1)
        dbg.print_info("Terminating a process...")
        # proc.terminate()
        proc.kill()
        proc.wait()
        dbg.print_info("Process returncode: %d" % proc.returncode)
    flog.close()

if __name__ == "__main__":
    main()