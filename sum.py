print('*** Funcion sum y next ***')
lista = [1, 2,3,4,5]
resultado = sum(lista)
print(resultado)

# podemos proporcionar un valor inicial , esto lo que hace es que empieza el valor desde 20 no desde 0, entonces es 20 + la suma de la lista

resultado = sum(lista, 20)
print(resultado)

# el operador next 

#convertimos la lista en un iterador 
iterador = iter(lista)

#imprimimos el primer valor del iterador 
print(f'EL sigiuetne elemento del iterable: {next(iterador)}')
#si lo volvemos a pedir nos regresa el siguiente valor en la lista
print(f'EL sigiuetne elemento del iterable: {next(iterador)}')
#si lo volvemos a pedir nos regresa el siguiente valor en la lista
print(f'EL sigiuetne elemento del iterable: {next(iterador)}')
#si lo volvemos a pedir nos regresa el siguiente valor en la lista
print(f'EL sigiuetne elemento del iterable: {next(iterador)}')
