#decoradores.py

print (' *** decoradores.py ***')

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print ('Antes de llamar a la funcion de saludar')
        resultado = funcion(*args, **kwargs)
        print('Despues de llamar a la funcion saludar')
        return resultado
    return wrapper
        
@decorador
def saludar(nombre):
    print (f'Hola {nombre}')

saludar('carlos')