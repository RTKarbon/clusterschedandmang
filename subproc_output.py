#!/usr/bin/env python

import subprocess
import shlex
from lib import *

def main():
    program_l = ["program1", "program2", "program3"]
    flog = open("program_log.txt", 'w')
    for pname in program_l:
        cmd = "python ./programs/%s.py" % pname
        proc = subprocess.Popen(shlex.split(cmd), stdout=flog)
        proc.wait()
    flog.close()

if __name__ == "__main__":
    main()