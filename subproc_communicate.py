#!/usr/bin/env python

import subprocess
import shlex, sys
from lib import *

def main():
    program_l = ["program1"]
    # flog = open("program_log.txt", 'w')
    flog = sys.stdout
    for pname in program_l:
        cmd = "python ./programs/%s.py" % pname
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, err) = proc.communicate()
        dbg.print_info("%s OUTPUT >>>\n%s>>>" % (pname, out), flog)
        dbg.print_info("%s ERROR: %s" % (pname, err), flog)
    flog.close()

if __name__ == "__main__":
    main()