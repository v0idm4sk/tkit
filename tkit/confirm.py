from . import colors

def confirm(txt, **opt):
    yes_val = opt.get("yes", "y")
    no_val = opt.get("no", "n")
    if_val = opt.get("ifv", True)
    else_val = opt.get("elsev", False)

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
        
    prompt_text = (
        f"{start_style}{txt} ({yes_val}/{no_val}){reset_code} "
    )

    while True:
        inp = input(prompt_text).strip().lower() 
        
        if inp == str(yes_val).lower():
            return if_val 
        elif inp == str(no_val).lower():
            return else_val