import time # Importamos 'time' para poder pausar la ejecución y ver el progreso

def progress(txt, **opt):
    """
    Simula una barra de progreso simple en la consola.
    """
    # Recoger y convertir los argumentos opcionales
    type_progress = opt.get("type", "/")
    value_prg = int(opt.get("value", 0))
    max_prg = int(opt.get("max", 100))

    if txt:
        if type_progress == "/":
            # Usamos range() para generar números desde value_prg hasta max_prg - 1
            # El for de Python itera sobre cada número en ese rango.
            for i in range(value_prg, max_prg):
                # i tomará el valor de la variable de progreso en cada iteración
                # Se imprime el texto junto con el número actual y un separador
                print(f"{txt} {i} / {max_prg}", end="\r", flush=True)
                time.sleep(0.05) # Pequeña pausa para simular el progreso
            
            # Una vez que el bucle termina, imprimimos el 100% o el máximo
            print(f"{txt} {max_prg} / {max_prg} - ¡Completado! 😊")

# ---
## Ejemplo de Uso
progress("Cargando datos") 

print("\n") # Imprime una línea nueva después del progreso
progress("Procesando archivos", value=10, max=50)