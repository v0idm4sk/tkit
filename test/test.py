# Asume que tu función printer y el diccionario txt_style están importados correctamente
# (ej. from tkit.args import printer)

# NOTA: Debes asegurarte de importar correctamente 'printer'
# Aquí simulamos la importación.
try:
    from tkit.printer import printer 
except ImportError:
    print("Error: Asegúrate de que 'printer' está en tkit/args.py y las rutas están correctas.")
    sys.exit(1)


def test_printer_function():
    print("\n--- INICIO de la Prueba de Colores y Estilos ---")

    # 1. PRUEBAS DE COLORES BÁSICOS
    printer("1. Texto Rojo:", color="red")
    printer("2. Texto Verde Brillante:", color="light-green")
    printer("3. Texto Magenta:", color="magenta")
    printer("4. Texto Blanco Brillante:", color="light-white", end="\n\n")

    # 2. PRUEBAS DE ESTILOS DE TEXTO
    printer("5. Texto en NEGRITA (Bold)", style="bold")
    printer("6. Texto SUBRAYADO (Underline)", style="underline")
    printer("7. Texto en CURSIVA (Italic)", style="italic")
    printer("8. Texto Tachado (Strikethrough)", style="strikethrough", end="\n\n")

    # 3. PRUEBAS DE FONDOS
    printer("9. Fondo Amarillo Básico", color="black", bg="yellow")
    printer("10. Fondo Azul Brillante", color="white", bg="light-blue", end="\n\n")

    # 4. PRUEBAS DE COMBINACIONES
    printer(
        "11. Combinación: Rojo Brillante, Fondo Negro, Negrilla y Subrayado", 
        color="light-red", 
        bg="black", 
        style="bold"
    )
    printer(
        "12. Combinación: Texto Blanco, Fondo Magenta Brillante, Invertido (Reverse)", 
        color="white", 
        bg="light-magenta", 
        style="reverse"
    )
    
    # 5. PRUEBAS DE MÚLTIPLES ARGUMENTOS
    printer("\n13. Mensaje con", "múltiples", "argumentos", "y color azul.", color="blue")
    
    print("\n--- FIN de la Prueba de Colores y Estilos ---")


if __name__ == "__main__":
    import sys
    # Esto asegura que solo se ejecute la prueba de la función printer
    test_printer_function()