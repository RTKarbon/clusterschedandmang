
import subprocess, sys, shlex
import dbglib as dbg

class Task:
    def __init__(self, cmd):
        self.proc = None
        self.cmd = cmd
        self.flog = sys.stdout
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


