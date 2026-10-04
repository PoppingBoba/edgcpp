#!/bin/python3

import os
import subprocess
import sys

args = sys.argv[1:]
tool = args[0]

if not os.path.isabs(tool):
    tool = os.path.abspath(tool) 

args[0] = tool

print(args)

subprocess.check_call(args)