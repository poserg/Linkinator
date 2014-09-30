#!/usr/bin/env python3

from core import run
from gui import run_gui
from sys import argv

if len(argv) == 2 and argv[1] == '--help':
    print ("linkinator --help")
    print ("linkinator <source-path> <destination-path>")
    print ("linkinator")
elif len(argv) == 3:
    p = argv[1:]
    run(p[0], p[1])
else:
    run_gui(run)
