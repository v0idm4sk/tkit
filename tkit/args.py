import sys

class Command:
    def __init__(self, **opt):
        self.command_names = opt.get("command", "").split()
        self.func = opt.get("func", lambda: None)
        self.arguments_names = opt.get("arguments", "").split()
        self.require_args = opt.get("require_args", False)
        self.exception_msg = opt.get("exception", "")

        cli_args = sys.argv[1:]

        command_is_called = bool(set(self.command_names) & set(cli_args))

        if command_is_called:
            try:
                cmd_index = cli_args.index(self.command_names[0])
                passed_args = cli_args[cmd_index + 1:] 
            except ValueError:
                passed_args = []
            if self.require_args:
                if len(passed_args) >= len(self.arguments_names):
                    self.func(*passed_args)
                else:
                    final_msg = self.exception_msg or "The arguments are insufficient! Required: " + ", ".join(self.arguments_names)
                    print(f"\033[31m× \033[0mTKit: \033[31mArgs Error: \033[0m{final_msg}")
            else:
                if passed_args:
                     self.func(*passed_args)
                else:
                     self.func()