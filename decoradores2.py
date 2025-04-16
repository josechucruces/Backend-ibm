#decoradores , aqui muestro la utilizcion real de un decorador para Registro de llamadas (logging)

import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def esperar():
    time.sleep(3)
    
esperar()