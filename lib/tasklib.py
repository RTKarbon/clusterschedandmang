
import subprocess, sys, shlex, re, os
import dbglib as dbg

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = os.path.join(SCRIPT_DIR, "../log")
BUILD_DIR = os.path.join(SCRIPT_DIR, "../build")

class Task:
    def __init__(self, cmd, tag=None):
        self.tag = tag
        self.proc = None
        self.cmd = cmd
        self.flog = sys.stdout
        self.log_path = os.path.join(LOG_DIR, self.tag + ".log")
        self.rv = None
        self.out = None
        self.err = None

    def Launch(self):
        proc = subprocess.Popen(shlex.split(self.cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.proc = proc
        return proc

    def WaitTillFinished(self):
        (out, err) = self.proc.communicate()
        rv = self.proc.returncode
        (self.rv, self.out, self.err) = (rv, out, err)
        return (rv, out, err)

class TaskGroup:
    def __init__(self):
        self.task_l = list()

    def AddTask(self, task):
        self.task_l.append(task)

    def LaunchInParallel(self):
        dbg.print_info("Launching tasks...")
        for task in self.task_l:
            task.Launch()

    def WaitForAll(self):
        dbg.print_info("Waiting for tasks to finish...")
        for task in self.task_l:
            task.WaitTillFinished()


