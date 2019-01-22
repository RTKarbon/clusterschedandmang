
import subprocess, sys, shlex, re
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

    def LaunchSlurm(self):
        fslurm_name = self.tag + ".slurm"
        fslurm_path = os.path.join(BUILD_DIR, fslurm_name)
        fslurm = open(fslurm_name, 'w')
        fslurm.write("#!/bin/sh\n")
        fslurm.write("#SBATCH -N 1\n")
        fslurm.write("#SBATCH --ntasks-per-node=1\n")
        fslurm.write("#SBATCH --mem=1G\n")
        fslurm.write("#SBATCH -t 30")
        fslurm.write("%s >> %s.log 2>&1" % (self.cmd, self.log_path))
        fslurm.close()
        os.chmod(fslurm_path, st.st_mode | stat.S_IEXEC)

        cmd = "sbatch %s" % fslurm_path
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        if proc.returncode != 0:
            dbg.print_error("Slurm command Failed!")

        match = re.search(r"Submitted batch job (\d+)", out)
        if match != None:
            self.job_id = int(match.group(1))
            dbg.print_info("Launched Slurm job %d" % self.job_id)
        else:
            dbg.print_error("Can't find Job ID in %s" % fslurm_path)


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


