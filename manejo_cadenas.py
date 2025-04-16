# manejo de cadenas

# dividir una cadena split() (parsing)

cadena = 'Hola Mundo'
palabras = cadena.split(' ')
print(palabras)
# buscar y reemplazar

#find en cadenas, buscar posiciones de cadenas
posicion = cadena.find('Mundo')
print (f'Posicion de la palabra Mundo, esta en la posición {posicion}')

#replace en cadenas, sustituir palabras en cadenas
nueva_cadena = cadena.replace('Mundo','Perro')
print (nueva_cadena)

#multiplicacion de cadenas
cadena =' Hola '
cadena_multiplicada = cadena * 3
print(cadena_multiplicada)

#strip es para limpiar una cedens , limpia al prinpio y al final, si no incluimos caracter limpia los espacios en blanco
cadena= '....Hola Mundo.......'
cadena_limpia= cadena.strip(' . ')
print(cadena_limpia)
