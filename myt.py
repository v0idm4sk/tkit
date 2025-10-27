import itertools
import time
import math # Para las conversiones de bytes

# --- Configuraciones Globales ---

# 1. Ciclo de símbolos para el spinner simple (type='/')
SPINNER = itertools.cycle(['/', '-', '\\', '|'])

# 2. Símbolos braille para el loader Braille (type=':')
BRAILLE_SPINNER = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])

# 3. Diccionario de prefijos de bytes
BYTE_PREFIXES = {
    'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4
}

# --- Función Principal ---

def progress(txt, **opt):
    """
    Muestra un loader o barra de progreso. SOLO imprime el 'txt' del usuario
    seguido del elemento de progreso (spinner, barra, valor), SIN texto adicional.
    """
    # 1. Obtener opciones con valores predeterminados
    type_progress = opt.get("type", "/")
    value_prg = opt.get("value", 0)
    max_prg = opt.get("max", 100)
    unit = opt.get("unit", "MB")
    
    try:
        value_prg = float(value_prg)
        max_prg = float(max_prg)
    except (ValueError, TypeError):
        # Si hay error en los valores, simplemente imprime el texto y sale
        print(f"{txt} Error en valores.", end="\r")
        return

    loader_output = "" # Solo contendrá el símbolo/valor/barra
    
    # 2. Lógica para cada tipo de loader (sin texto descriptivo)

    # Opción: Spinner simple (/)
    if type_progress == "/":
        loader_output = next(SPINNER)
    
    # Opción: Loader Braille (:)
    elif type_progress == ":":
        loader_output = next(BRAILLE_SPINNER)
        
    # Opción: Porcentaje (%)
    elif type_progress == "%":
        percentage = (value_prg / max_prg) * 100 if max_prg else 0
        loader_output = f"{percentage:.1f}%"
        
    # Opción: Valor simple (1) - Ejemplo: 3 / 245
    elif type_progress == "1":
        loader_output = f"{int(value_prg)}/{int(max_prg)}"
    
    # Opción: Barra de carga (||)
    elif type_progress == "||":
        BAR_LENGTH = 20
        progress_ratio = value_prg / max_prg if max_prg else 0
        filled_length = int(BAR_LENGTH * progress_ratio)
        bar = '█' * filled_length + '░' * (BAR_LENGTH - filled_length)
        percentage = progress_ratio * 100
        loader_output = f"[{bar}] {percentage:.1f}%"

    # Opción: Valor en Bytes ([caracter]b)
    elif type_progress.endswith("b"):
        byte_unit = type_progress[:-1].upper() 
        display_unit = unit.upper() if byte_unit not in BYTE_PREFIXES else byte_unit

        divisor = BYTE_PREFIXES.get(display_unit, 1024**2) 
        
        display_value = value_prg / divisor
        display_max = max_prg / divisor
        
        loader_output = f"{display_value:.2f}/{display_max:.2f}{display_unit}"

    # Opción: Velocidad de Internet (s)
    elif type_progress == "s":
        speed = value_prg 
        speed_unit = unit.upper()
        loader_output = f"{speed:.2f}{speed_unit}/s"


    # 3. Impresión Final
    # Concatenamos el texto del usuario y el loader_output (separados por un espacio)
    output = f"{txt} {loader_output}"
    print(output, end="\r", flush=True)

    # 4. Manejo de fin de proceso para limpiar la línea
    if max_prg > 0 and value_prg >= max_prg:
        # Imprime solo el texto del usuario seguido de un emoji de fin y muchos espacios
        print(f"{txt} ✅{' ' * (len(loader_output) + 5)}") # Agrega espacios para borrar el rastro
        
# ----------------------------------------------------------------------
## Ejemplos de Uso (Nota: El usuario debe poner el texto descriptivo si lo quiere)

# Simulación de un proceso
TOTAL_STEPS = 40

print("\n--- Spinner (/) y Braille (:) ---")
for i in range(TOTAL_STEPS + 1):
    # El usuario pone el texto "Cargando..." y la función añade el spinner
    progress("Cargando archivos", type="/") 
    time.sleep(0.05)

for i in range(TOTAL_STEPS + 1):
    # El usuario pone el texto "Compilando:" y la función añade el braille
    progress("Compilando:", type=":")
    time.sleep(0.05)

print("\n--- Barra (||) y Porcentaje (%) ---")
for i in range(TOTAL_STEPS + 1):
    # El usuario pone el texto "Progreso total" y la función añade la barra
    progress("Progreso total", type="||", value=i, max=TOTAL_STEPS)
    time.sleep(0.05)

for i in range(TOTAL_STEPS + 1):
    # El usuario pone el texto "Completado" y la función añade el porcentaje
    progress("Completado", type="%", value=i, max=TOTAL_STEPS)
    time.sleep(0.05)
    
print("\n--- Bytes (mb) y Valor (1) ---")
# Simulación de una descarga de 500 MB
TOTAL_BYTES = 500 * (1024**2) 
for i in range(TOTAL_STEPS + 1):
    current_bytes = (i / TOTAL_STEPS) * TOTAL_BYTES
    # El usuario especifica la unidad con el texto:
    progress("Descarga actual:", type="mb", value=current_bytes, max=TOTAL_BYTES)
    time.sleep(0.05)
    
print("\n--- Velocidad (s) ---")
for i in range(1, 10):
    speed_kb = i * 200
    # El usuario añade el texto "Velocidad de red:"
    progress("Velocidad de red:", type="s", value=speed_kb, unit="KB")
    time.sleep(0.1)