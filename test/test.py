import tkit

def help_func():
    print("Help XD")

help_cmd = tkit.args.Command(
    command = "help",
    func = help_func
)