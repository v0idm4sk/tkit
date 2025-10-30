"""
from . import colors

def ulist(obj, **opt):
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
    indent_spaces = opt.get("indent_spaces", 2)
    
    def _process_obj(data, current_level=0):
        indent = " " * (current_level * indent_spaces)
        result = []

        for key, value in data.items():
            if isinstance(value, dict):
                result.append(f"{indent}- {key}:")
                
                nested_list = _process_obj(value, current_level + 1)
                result.extend(nested_list)
                
            else:
                if value == "":
                    result.append(f"{indent}- {key}.")
                else:
                    result.append(f"{indent}- {key}: {value}.")
                    
        return result

    dscrptn = _process_obj(obj, 0)
    
    for line in dscrptn:
        return f"{start_style}{line}{reset_code}"
        

def olist(obj, **opt):
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
        
    indent_spaces = opt.get("indent_spaces", 2)
    
    def _process_obj(data, current_level=0, start_count=1):
        indent = " " * (current_level * indent_spaces)
        result = []
        current_count = start_count

        for key, value in data.items():
            line_prefix = f"{current_count}."
            
            if isinstance(value, dict):
                result.append(f"{indent}{line_prefix} {key}:")
                
                nested_list = _process_obj(value, current_level + 1, start_count=1)
                result.extend(nested_list)
                
            else:
                if value == "":
                    result.append(f"{indent}{line_prefix} {key}.")
                else:
                    result.append(f"{indent}{line_prefix} {key}: {value}.")
            
            current_count += 1
                    
        return result, current_count

    dscrptn, final_count = _process_obj(obj, 0)
    
    for line in dscrptn:
        return f"{start_style}{line}{reset_code}"
        
def table(obj, **opt):
    if isinstance(obj, dict):
        print()
"""        