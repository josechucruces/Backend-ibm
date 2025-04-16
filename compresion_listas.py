cuadrados = []

for x in range (1, 6):
    cuadrados.append(x**2)
print (cuadrados)    
## Es lo mismo el de arriba que lo de abajo , como el de arriba no se hace, se hace como el de abajo


cuadrados = [x**2 for x in range(10)]
print (cuadrados)

## Y si hacemos una lista por comprension con una condicion :
cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print (cuadrados)

## Y si es un if con un else es asi ... 
clasificacion = ["par" if x % 2 == 0 else "impar" for x in range (5)]
print(clasificacion)

#producto cartesiano de dos listas, que quiere decir todo por todo, todas las combincaciones posibles de algo
colores = ['rojo', 'verde']
tallas = ['S', 'M', 'L']
combinaciones = [(color, talla) for color in colores for talla in tallas]
print(combinaciones)

#aplanar una matriz
matriz = [[1,2,3], [4,5,6], [7,8,9]]
plana = [num for fila in matriz for num in fila]
print(plana)

#extraer vocales en una cadena
cadena = "Listas por comprension en Python"
vocales = [c for c in cadena.lower() if c in 'aeiouáéí´óú']
print(vocales)

#convertidor de temperatura
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)

matriz_identidad = [[1 if i == j else 0 for j in range (3)] for i in range(3)]
print(matriz_identidad)

