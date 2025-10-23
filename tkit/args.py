import sys
import numpy as np

class Command:
    def __init__(self, *args, **opt):
        self.command = opt["command"].split()
        self.func = ""

        if np.any(np.isin(np.array(sys.argv), np.array(opt["command"].split()))):
            if (opt["req_args"], opt["require_args"]) == True:
                if np.all(np.isin(np.array(sys.argv), np.array(opt["arguments"].split()))):
                    opt["func"](*opt["arguments"].split())
                else:
                    print("\033[31m× \033[0mTKit: \033[31mArgs Error: \033[0mThe arguments are insufficient!\nYou have 2 options:\n  - 1. Declare 'require-args' as False.\n  - 2. Add an exception message (with the argument 'exception').")
            else:
                if np.any(np.isin(np.array(sys.argv), np.array(opt["arguments"].split()))):
                    opt["func"](*opt["arguments"].split())
                else:
                    print("\033[31m× \033[0mTKit: \033[31mArgs Error: \033[0mThe arguments are insufficient!\nYou have 2 options:\n  - 1. Declare 'require-args' as False.\n  - 2. Add an exception message (with the argument 'exception').")