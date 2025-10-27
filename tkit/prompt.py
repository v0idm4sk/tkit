from . import colors
import getpass # Importamos getpass para manejar entradas secretas

class prompt:
    def __init__(self, txt, **opt):
        # 1. Códigos de estilo base
        reset_code = colors.txt_style.get("reset", "\033[0m")
        
        # --- Obtener Estilos de la PREGUNTA (txt) ---
        start_style_q = ""
        for name, key in [("color", "color"), ("bg", "background"), ("style", "style")]:
            value = opt.get(name)
            style_dict = colors.txt_style.get(key, {})
            if value in style_dict:
                start_style_q += style_dict[value]

        # --- Manejo de Espacios de Separación y Formato del Mensaje ---
        spaces_value = opt.get("in-spaces", 1)
        try:
            spaces_count = int(spaces_value)
        except ValueError:
            spaces_count = 1
            
        separator = " " * spaces_count
        prompt_question = f"{start_style_q}{txt}{separator}"
        
        # --- Obtener Estilos de la ENTRADA del Usuario (Input) ---
        start_style_in = ""
        for name, key in [("color-in", "color"), ("bg-in", "background"), ("style-in", "style")]:
            value = opt.get(name)
            style_dict = colors.txt_style.get(key, {})
            if value in style_dict:
                start_style_in += style_dict[value]
        
        # --- Realizar la Petición de Entrada ---
        
        # 1. Imprimir la pregunta y el estilo de la entrada (sin el salto de línea)
        print(prompt_question, end="")
        
        # 2. Capturar la entrada. El estilo se aplica AL PROMPT, no a lo que escribes.
        # Solo aplicamos el estilo *antes* del input y lo reseteamos *después*.
        # Esto solo funciona si el input() está vacio o con el código ANSI.
        
        if opt.get("secret", False):
            # Usar getpass para claves (sin mostrar el texto)
            # NOTA: getpass no admite que le pasemos un prompt ya formateado con ANSI.
            # Debe usarse el print() previo.
            raw_input = getpass.getpass(prompt=f"{start_style_in}{reset_code}")
        else:
            # Entrada normal con los códigos ANSI deseados.
            raw_input = input(f"{start_style_in}{reset_code}")
        
        # --- Asignación de Atributos (CORREGIDA) ---
        self.value = raw_input
        self.color = opt.get("color")
        self.bg = self.background = opt.get("bg")
        self.style = opt.get("style")
        
        self.color_in = opt.get("color-in")
        self.bg_in = self.background_in = opt.get("bg-in")
        self.style_in = opt.get("style-in")