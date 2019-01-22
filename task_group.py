#!/usr/bin/env python

import subprocess
import shlex
from lib import *

def main():
    program_l = ["program1", "program2", "program3"]
    task_gr = tsk.TaskGroup()
    # Create Tasks
    for pname in program_l:
        cmd = "python ./programs/%s.py" % pname
        task_gr.AddTask(tsk.Task(cmd))
    # Launch Tasks
    task_gr.LaunchInParallel()
    # Wait for Tasks
    task_gr.WaitForAll()


if __name__ == "__main__":
    main()