import os, sys

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
LIB_DIR = os.path.join(SCRIPT_DIR, "..")
sys.path.insert(0, LIB_DIR)

from lib import *