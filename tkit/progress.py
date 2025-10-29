import itertools
import time
import math



def progress(txt, **opt):
    SPINNER = itertools.cycle(['/', '-', '\\', '|'])
    BRAILLE_SPINNER = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
    BYTE_PREFIXES = {
        'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4
    }
    
    type_progress = opt.get("type", "/")
    value_prg = opt.get("value", 0)
    max_prg = opt.get("max", 100)
    unit = opt.get("unit", "B")
    
    
    out_action = opt.get("out", "leave") 
    
    try:
        value_prg = float(value_prg)
        max_prg = float(max_prg)
    except (ValueError, TypeError):
        print(f"{txt} Error: 'value' y 'max' deben ser numéricos.", end="\r")
        return

    loader_output = ""
    progress_ratio = value_prg / max_prg if max_prg else 0
    percentage = progress_ratio * 100

    
    if type_progress == "/":
        loader_output = next(SPINNER)
    elif type_progress == ":":
        loader_output = next(BRAILLE_SPINNER)
    elif type_progress == "%":
        loader_output = f"{percentage:.1f}%"
    elif type_progress == "1":
        loader_output = f"{int(value_prg)}/{int(max_prg)}"
    elif type_progress == "||":
        BAR_LENGTH = 20
        filled_length = int(BAR_LENGTH * progress_ratio)
        bar = '█' * filled_length + '░' * (BAR_LENGTH - filled_length)
        loader_output = f"[{bar}] {percentage:.1f}%"
    elif type_progress.endswith("b"):
        byte_unit = type_progress[:-1].upper() 
        display_unit = unit.upper() if byte_unit not in BYTE_PREFIXES else byte_unit
        divisor = BYTE_PREFIXES.get(display_unit, 1)
        display_value = value_prg / divisor
        display_max = max_prg / divisor
        loader_output = f"{display_value:.2f}/{display_max:.2f}{display_unit}"
    elif type_progress == "s":
        speed = value_prg 
        speed_unit = unit.upper()
        loader_output = f"{speed:.2f}{speed_unit}/s"

    
    output = f"{txt} {loader_output}"
    print(output, end="\r", flush=True)

    
    if max_prg > 0 and value_prg >= max_prg:
        
        
        if isinstance(out_action, str) and out_action.lower() == 'leave':
            print() 
            
        elif isinstance(out_action, str) and out_action.lower() == 'success':
            clear_spaces = ' ' * (len(loader_output) + 5)
            print(f"{txt} ✅{clear_spaces}")
            
        elif isinstance(out_action, str) and out_action.lower() == 'clear':
            full_line_length = len(output)
            print(f"{' ' * full_line_length}", end="\r\n")
            
        
        elif isinstance(out_action, str):
            
            clear_spaces_needed = len(output) - len(out_action)
            
            if clear_spaces_needed < 0: clear_spaces_needed = 0 
            
            
            print(f"{out_action}{' ' * clear_spaces_needed}")
        else:
             print() 
