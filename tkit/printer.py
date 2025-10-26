from . import colors

def printer(*args, **opt):
    start_style = ""
    reset_code = colors.txt_style.get("reset", "\033[0m")
    
    color_name = opt.get("color")
    if color_name in colors.txt_style.get("color", {}):
        start_style += colors.txt_style["color"][color_name]

    bg_name = opt.get("bg")
    if bg_name in colors.txt_style.get("background", {}):
        start_style += colors.txt_style["background"][bg_name]

    style_name = opt.get("style")
    if style_name in colors.txt_style.get("style", {}):
        start_style += colors.txt_style["style"][style_name]
    
    message = " ".join(map(str, args))

    print(
        f"{start_style}{message}{reset_code}",
        end=opt.get("end", "\n"),
        flush=opt.get("flush", False)
    )