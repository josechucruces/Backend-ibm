print ('funciones lambda')

#funcion numero por dos sin usar lambda

def num_por_dos(x):
    return x * 2
    
print (num_por_dos(5))

#funcion lambda (anonima )

num_por_dos_lamda = lambda x: x * 2

print (f' El numero 2 por 2 es : {num_por_dos_lamda(2)}') 
print (f' El numero 4 por 2 es : {num_por_dos_lamda(4)}') 


numeros = [1,2,3,4,5,6,7,8]
cuadrados = list(map(lambda x: x**2, numeros))
print (cuadrados)

## para filtrar en una lista con alguna condicion, en este caso que sea par
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)


## aqui ordenamos una lista

personas = [
    {"nombre": "ana", "edad": 30},
    {"nombre": "luis", "edad": 25},
    {"nombre": "Carlos", "edad": 40}
]
ordenadas = sorted(personas, key=lambda p: p["edad"])
print(ordenadas)

